Summary:	An extended version of DVIPDFMx with support for XeTeX output
Summary(pl.UTF-8):	Rozszerzona wersja DVIPDFMx przetwarzająca wyjście XeTeXa
Name:		xdvipdfmx
Version:	0.4
Release:	1
License:	GPL
Group:		Applications/Publishing/TeX
Source0:	http://scripts.sil.org/svn-view/xdvipdfmx/TAGS/%{name}-%{version}.tar.gz
# Source0-md5:	2bb9d65f2406a112fa53dbd0697d93ad
URL:		http://scripts.sil.org/xetex_linux
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel
BuildRequires:	kpathsea-devel
BuildRequires:	libpaper-devel
BuildRequires:	libpng-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xdvipdfmx is an output driver for the XeTeX typesetting system. It is
an extended version of DVIPDFMx by Jin-Hwan Cho and Shunsaku Hirata,
which is itself an extended version of dvipdfm by Mark A. Wicks. This
driver converts XDV (extended DVI) output from the xetex program into
standard PDF that can be viewed or printed.

%description -l pl.UTF-8
xdvipdfmx jest sterownikiem przetwarzającym wyjście systemu składu
XeTeX. To jest rozszerzona wersja DVIPDFMx autorstwa Jin-Hwan Cho
i Shunsaku Hirata, która z kolei jest rozszerzoną wersją dvipdfm
autorstwa Marka A. Wicksa. Ten sterownik konwertuje wyjście programu
xetex z formatu XDV (rozszerzony DVI) na standardowy format PDF,
który może być oglądany bądź drukowany.

%prep
%setup -q

%build
sh ./configure \
	--with-freetype2=`freetype-config --prefix`
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install src/xdvipdfmx $RPM_BUILD_ROOT%{_bindir}

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xdvipdfmx

%clean
rm -rf $RPM_BUILD_ROOT
