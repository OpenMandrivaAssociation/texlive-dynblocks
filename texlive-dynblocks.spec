# revision 27838
# category Package
# catalog-ctan /macros/latex/contrib/beamer-contrib/dynblocks
# catalog-date 2012-09-27 16:18:28 +0200
# catalog-license lppl1.3
# catalog-version 0.2a
Name:		texlive-dynblocks
Version:	0.2a
Release:	2
Summary:	A simple way to create dynamic blocks for Beamer
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/beamer-contrib/dynblocks
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dynblocks.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dynblocks.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Fri Oct 26 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.2a-1
+ Revision: 819980
- Update to latest release.

* Thu Aug 09 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.1-1
+ Revision: 813471
- Import texlive-dynblocks
- Import texlive-dynblocks

