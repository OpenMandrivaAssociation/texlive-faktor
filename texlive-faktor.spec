# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/faktor
# catalog-date 2007-02-27 14:19:10 +0100
# catalog-license lppl
# catalog-version 0.1b
Name:		texlive-faktor
Version:	0.1b
Release:	2
Summary:	Typeset quotient structures with LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/faktor
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/faktor.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/faktor.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/faktor.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides the means to typeset factor structures, as
are used in many areas of algebraic notation. The structure is
similar to the 'A/B' that is provided by the nicefrac package
(part of the units distribution), and by the xfrac package; the
most obvious difference is that the numerator and denominator's
sizes do not change in the \faktor command.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/faktor/faktor.sty
%doc %{_texmfdistdir}/doc/latex/faktor/README
%doc %{_texmfdistdir}/doc/latex/faktor/faktor.pdf
#- source
%doc %{_texmfdistdir}/source/latex/faktor/faktor.dtx
%doc %{_texmfdistdir}/source/latex/faktor/faktor.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
