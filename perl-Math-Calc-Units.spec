#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Math
%define		pnam	Calc-Units
Summary:	Math::Calc::Units - human-readable unit-aware calculator
Summary(pl.UTF-8):	Math::Calc::Units - kalkulator obsługujący jednostki
Name:		perl-Math-Calc-Units
Version:	1.07
Release:	1
License:	GPL v2 or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Math/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	56e4be0e64d6c8fc27c8f87d0d3cebd8
URL:		http://search.cpan.org/dist/Math-Calc-Units/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Math::Calc::Units is a simple calculator that keeps track of units. It
currently handles combinations of byte sizes and duration only,
although adding any other multiplicative types is easy. Any unknown
type is treated as a unique user type (with some effort to map English
plurals to their singular forms).

The primary intended use is via the ucalc script that prints out all
of the "readable" variants of a value. For example, "3 bytes" will
only produce "3 byte", but "3 byte / sec" produces the original along
with "180 byte / minute", "10.55 kilobyte / hour", etc.

%description -l pl.UTF-8
Math::Calc::Units to prosty kalkulator zachowujący jednostki.
Aktualnie obsługuje tylko kombinacje rozmiaru w bajtach i czasu, ale
dodanie dowolnych typów multiplikatywnych jest proste. Każdy nieznany
typ jest traktowany jako unikalny typ użytkownika (z próbą zamiany
angielskich form mnogich na pojedyncze).

Podstawowy sposób użycia to skrypt ucalc, wypisujący wszystkie
"czytelne" warianty wartości. Na przykład "3 bytes" daje tylko "3
byte", ale "3 byte / sec" daje wartość oryginalną oraz "180 byte /
minute", "10.55 kilobyte / hour" itd.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes LICENSE README
%attr(755,root,root) %{_bindir}/*
%{perl_vendorlib}/Math/Calc/Units.pm
%{perl_vendorlib}/Math/Calc/Units
%{_mandir}/man3/*
