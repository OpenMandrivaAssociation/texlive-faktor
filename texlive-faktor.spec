Name:		texlive-faktor
Version:	15878
Release:	2
Summary:	Typeset quotient structures with LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/faktor
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/faktor.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/faktor.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/faktor.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
