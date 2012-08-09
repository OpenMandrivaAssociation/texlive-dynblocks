# revision 26428
# category Package
# catalog-ctan /macros/latex/contrib/beamer-contrib/dynblocks
# catalog-date 2012-05-14 22:52:16 +0200
# catalog-license lppl1.3
# catalog-version 0.1
Name:		texlive-dynblocks
Version:	0.1
Release:	1
Summary:	A simple way to create dynamic blocks for Beamer
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/beamer-contrib/dynblocks
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dynblocks.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dynblocks.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
The package provides full customisation of the aspect and
dimensions of blocks inside a presentation.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/dynblocks/README
%doc %{_texmfdistdir}/doc/latex/dynblocks/doc/dynblocks.pdf
%doc %{_texmfdistdir}/doc/latex/dynblocks/doc/dynblocks.tex
%doc %{_texmfdistdir}/doc/latex/dynblocks/doc/images/alert_1.pdf
%doc %{_texmfdistdir}/doc/latex/dynblocks/doc/images/alert_2.pdf
%doc %{_texmfdistdir}/doc/latex/dynblocks/doc/images/align.pdf
%doc %{_texmfdistdir}/doc/latex/dynblocks/doc/images/basic_1.pdf
%doc %{_texmfdistdir}/doc/latex/dynblocks/doc/images/basic_2.pdf
%doc %{_texmfdistdir}/doc/latex/dynblocks/doc/images/cmbx_1.pdf
%doc %{_texmfdistdir}/doc/latex/dynblocks/doc/images/cmbx_2.pdf
%doc %{_texmfdistdir}/doc/latex/dynblocks/doc/images/cmby_1.pdf
%doc %{_texmfdistdir}/doc/latex/dynblocks/doc/images/cmby_2.pdf
%doc %{_texmfdistdir}/doc/latex/dynblocks/doc/images/custcol_1.pdf
%doc %{_texmfdistdir}/doc/latex/dynblocks/doc/images/custcol_2.pdf
%doc %{_texmfdistdir}/doc/latex/dynblocks/doc/images/custcol_3.pdf
%doc %{_texmfdistdir}/doc/latex/dynblocks/doc/images/custcol_4.pdf
%doc %{_texmfdistdir}/doc/latex/dynblocks/doc/images/estl.pdf
%doc %{_texmfdistdir}/doc/latex/dynblocks/doc/images/shdrndc_1.pdf
%doc %{_texmfdistdir}/doc/latex/dynblocks/doc/images/shdrndc_2.pdf
%doc %{_texmfdistdir}/doc/latex/dynblocks/doc/images/szeg_1.pdf
%doc %{_texmfdistdir}/doc/latex/dynblocks/doc/images/szeg_2.pdf
%doc %{_texmfdistdir}/doc/latex/dynblocks/latex/dynblocks.sty

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
