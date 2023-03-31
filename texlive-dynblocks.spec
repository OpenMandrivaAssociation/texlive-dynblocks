Name:		texlive-dynblocks
Version:	35193
Release:	2
Summary:	A simple way to create dynamic blocks for Beamer
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/beamer-contrib/dynblocks
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dynblocks.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dynblocks.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides full customisation of the aspect and
dimensions of blocks inside a presentation.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/dynblocks/dynblocks.sty
%doc %{_texmfdistdir}/doc/latex/dynblocks/README
%doc %{_texmfdistdir}/doc/latex/dynblocks/dynblocks.pdf
%doc %{_texmfdistdir}/doc/latex/dynblocks/dynblocks.tex
%doc %{_texmfdistdir}/doc/latex/dynblocks/images/alert_1.pdf
%doc %{_texmfdistdir}/doc/latex/dynblocks/images/alert_2.pdf
%doc %{_texmfdistdir}/doc/latex/dynblocks/images/align.pdf
%doc %{_texmfdistdir}/doc/latex/dynblocks/images/basic_1.pdf
%doc %{_texmfdistdir}/doc/latex/dynblocks/images/basic_2.pdf
%doc %{_texmfdistdir}/doc/latex/dynblocks/images/cmbx_1.pdf
%doc %{_texmfdistdir}/doc/latex/dynblocks/images/cmbx_2.pdf
%doc %{_texmfdistdir}/doc/latex/dynblocks/images/cmby_1.pdf
%doc %{_texmfdistdir}/doc/latex/dynblocks/images/cmby_2.pdf
%doc %{_texmfdistdir}/doc/latex/dynblocks/images/custcol_1.pdf
%doc %{_texmfdistdir}/doc/latex/dynblocks/images/custcol_2.pdf
%doc %{_texmfdistdir}/doc/latex/dynblocks/images/custcol_3.pdf
%doc %{_texmfdistdir}/doc/latex/dynblocks/images/custcol_4.pdf
%doc %{_texmfdistdir}/doc/latex/dynblocks/images/estl.pdf
%doc %{_texmfdistdir}/doc/latex/dynblocks/images/shdrndc_1.pdf
%doc %{_texmfdistdir}/doc/latex/dynblocks/images/shdrndc_2.pdf
%doc %{_texmfdistdir}/doc/latex/dynblocks/images/szeg_1.pdf
%doc %{_texmfdistdir}/doc/latex/dynblocks/images/szeg_2.pdf

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
