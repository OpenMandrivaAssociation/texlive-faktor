# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/faktor
# catalog-date 2007-02-27 14:19:10 +0100
# catalog-license lppl
# catalog-version 0.1b
Name:		texlive-faktor
Version:	0.1b
Release:	1
Summary:	Typeset quotient structures with LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/faktor
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/faktor.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/faktor.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/faktor.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package provides the means to typeset factor structures, as
are used in many areas of algebraic notation. The structure is
similar to the 'A/B' that is provided by the nicefrac package
(part of the units distribution), and by the xfrac package; the
most obvious difference is that the numerator and denominator's
sizes do not change in the \faktor command.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/faktor/faktor.sty
%doc %{_texmfdistdir}/doc/latex/faktor/README
%doc %{_texmfdistdir}/doc/latex/faktor/faktor.pdf
#- source
%doc %{_texmfdistdir}/source/latex/faktor/faktor.dtx
%doc %{_texmfdistdir}/source/latex/faktor/faktor.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
