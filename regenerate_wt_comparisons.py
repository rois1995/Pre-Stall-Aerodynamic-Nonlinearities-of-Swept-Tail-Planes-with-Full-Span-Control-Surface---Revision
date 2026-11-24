"""Rebuild Figs. 5, 11, 15 from frozen Phase-2B records.

Measured WT values and propagated pointwise error magnitudes are preserved.
The compressed source table is checksum-verified; no CFD or fitting is done.
"""
import base64, hashlib, io, zlib
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import pandas as pd

ROOT=Path(__file__).resolve().parent
blob=(ROOT/"revision_materials/reference_comparison_points_zlib64.txt").read_text().strip()
raw=zlib.decompress(base64.b64decode(blob))
assert hashlib.sha256(raw).hexdigest()=="6572f32c10ec3eddf60d854de336e1854068aaf4325c743f8714ec2a3a63904e"
df=pd.read_csv(io.BytesIO(raw))
assert len(df)==352 and set(df.panel)==set("abcdef")
plt.rcParams.update({"font.family":"DejaVu Serif","mathtext.fontset":"stix",
 "font.size":9.5,"axes.labelsize":10,"axes.titlesize":10,
 "xtick.labelsize":9.5,"ytick.labelsize":9.5,"legend.fontsize":9.5,
 "pdf.fonttype":42,"ps.fonttype":42,"axes.spines.top":False,
 "axes.spines.right":False,"lines.linewidth":1.1})
BLUE="#0072B2"; ORANGE="#D55E00"; GREEN="#009E73"; MS={20:"o",30:"s"}

def series(panel,key):
    z=df[(df.panel==panel)&(df.series==key)].sort_values("x")
    assert len(z)>0,(panel,key)
    return z

def wt_curve(ax,panel,key,color,d):
    z=series(panel,key)
    assert z.error.notna().all(),(panel,key)
    ax.plot(z.x,z.y,color=color,lw=1.0,zorder=2)
    ax.errorbar(z.x,z.y,yerr=z.error,fmt=MS[d],color=color,
       markersize=2.25,markeredgewidth=.35,elinewidth=1.05,
       capthick=1.0,capsize=2.5,linestyle="none",zorder=6)

def rans(ax,panel,d,color):
    direct = f"RANS_{d}_direct"
    reflected = f"RANS_{d}_reflected"
    points = df[(df.panel == panel) & (
        (df.series == direct) | ((df.series == reflected) & (df.x != 0))
    )].sort_values("x")
    assert points.x.is_unique and (points.x == 0).sum() == 1, (panel, d)
    ax.plot(points.x, points.y, color=color, marker=MS[d], markersize=3.0,
            markerfacecolor="white", linestyle="--", linewidth=1., zorder=3)

def axis(ax,quantity,title=None):
    ax.set(xlim=(-18.5,8.5),xticks=[-15,-10,-5,0,5],xlabel=r"$\alpha$ (deg)")
    ax.set_ylabel(r"$C_L$" if quantity=="CL" else r"$C_M^A$")
    ax.grid(alpha=.15,lw=.65)
    ax.axhline(0,color=".5",lw=.7,zorder=0)
    if title:ax.set_title(title)

def mark(ax,a,b,hatch=False):
    ax.axvspan(a,b,facecolor=".70",alpha=.16,zorder=0,
               hatch="///" if hatch else None,
               edgecolor=".5" if hatch else "none")

def legend(fig,entries,y=.01,ncol=4,fs=9.0):
    hands=[Line2D([],[],color=c,marker=MS[d],markersize=3.6,
                   markerfacecolor="white" if dashed else c,
                   linestyle="--" if dashed else "-",lw=1.0)
           for text,c,d,dashed in entries]
    fig.legend(hands,[e[0] for e in entries],loc="lower center",
      bbox_to_anchor=(.5,y),ncol=ncol,frameon=False,fontsize=fs,
      handlelength=1.5,columnspacing=1.0,handletextpad=.45)

def save(fig,name):
    fig.savefig(ROOT/name)
    plt.close(fig)

fig,axes=plt.subplots(1,2,figsize=(6.6,3.5))
fig.subplots_adjust(left=.14,right=.985,top=.85,bottom=.265,wspace=.46)
for ax,p,q,title in zip(axes,"ab",["CL","CM"],["(a) Lift","(b) Pitching moment"]):
    axis(ax,q,title)
    for d,c in [(20,BLUE),(30,ORANGE)]:
        rans(ax,p,d,c);wt_curve(ax,p,"WT_"+str(d),c,d)
    mark(ax,-2,0);mark(ax,-12,-8,hatch=True)
legend(fig,[(rf"WT, $\delta={d}^\circ$",c,d,False) for d,c in [(20,BLUE),(30,ORANGE)]]+
           [(rf"RANS, $\delta={d}^\circ$",c,d,True) for d,c in [(20,BLUE),(30,ORANGE)]],fs=8.9)
save(fig,"figures_revision_comparison.pdf")

for geometry,panels,color,out in [
    ("Dihedral","cd",GREEN,"figures_revision_comparison_dihedral.pdf"),
    ("Planform","ef",ORANGE,"figures_revision_comparison_planform.pdf")]:
    fig,ax=plt.subplots(2,2,figsize=(6.6,6.45))
    fig.subplots_adjust(left=.11,right=.985,top=.94,bottom=.13,wspace=.33,hspace=.46)
    for j,q in enumerate(["CL","CM"]):
        top,bot=ax[0,j],ax[1,j]
        p="ab"[j];other=panels[j]
        axis(top,q);axis(bot,q)
        for d in [20,30]:
            wt_curve(top,p,"WT_"+str(d),BLUE,d)
            wt_curve(top,other,"WT_"+str(d),color,d)
            col=BLUE if d==20 else ORANGE
            rans(bot,other,d,col);wt_curve(bot,other,"WT_"+str(d),col,d)
        for target in [top,bot]:
            if geometry=="Dihedral":
                # Table 5 assesses the same lift interval at both deflections.
                mark(target,-2,0)
                if q=="CM":
                    mark(target,-4,-2,hatch=True)
            else:mark(target,0,2)
    ax[0,0].set_title("Wind-tunnel "+geometry.lower()+" comparison",fontsize=10)
    ax[1,0].set_title(("Positive-dihedral" if geometry=="Dihedral" else "Forward-swept")+" WT--RANS",fontsize=10)
    if geometry=="Dihedral":
        upper=[(rf"$\Gamma={g}^\circ$, $\delta={d}^\circ$",c,d,False)
               for g,c in [(0,BLUE),(45,GREEN)] for d in [20,30]]
    else:
        upper=[(rf"{name}, $\delta={d}^\circ$",c,d,False)
               for name,c in [("Aft",BLUE),("Forward",ORANGE)] for d in [20,30]]
    hands=[Line2D([],[],color=c,marker=MS[d],markersize=3.6,lw=1.0)
           for text,c,d,dashed in upper]
    fig.legend(hands,[e[0] for e in upper],loc="upper center",
       bbox_to_anchor=(.5,.535),ncol=4,frameon=False,
       fontsize=8.7,columnspacing=.7,handlelength=1.25)
    lower=[(rf"WT, $\delta={d}^\circ$",BLUE if d==20 else ORANGE,d,False) for d in [20,30]]+[
           (rf"RANS, $\delta={d}^\circ$",BLUE if d==20 else ORANGE,d,True) for d in [20,30]]
    legend(fig,lower,y=.005,fs=8.7)
    save(fig,out)
print("Rebuilt Figs. 5, 11, 15 with pointwise propagated CL and CM WT bars")
