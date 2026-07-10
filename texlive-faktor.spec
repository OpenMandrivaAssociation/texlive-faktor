%global tl_name faktor
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1b
Release:	%{tl_revision}.1
Summary:	Typeset quotient structures with LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/faktor
License:	lppl1.3b
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/faktor.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/faktor.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/faktor.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides the means to typeset factor structures, as are used
in many areas of algebraic notation. The structure is similar to the
'A/B' that is provided by the nicefrac package (part of the units
distribution), and by the xfrac package; the most obvious difference is
that the numerator and denominator's sizes do not change in the \faktor
command.

