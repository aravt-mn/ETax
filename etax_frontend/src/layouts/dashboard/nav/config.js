// component
import SvgColor from '../../../components/svg-color';

// ----------------------------------------------------------------------

const icon = (name) => <SvgColor src={`/assets/icons/navbar/${name}.svg`} sx={{ width: 1, height: 1 }} />;

const navConfig = [
  {
    title: 'dashboard',
    path: '/dashboard/app',
    icon: icon('ic_analytics'),
  },
  {
    title: 'Баркодын жагсаалт',
    path: '/dashboard/barcode',
    icon: icon('ic_analytics'),
  },
  {
    title: 'Хэрэглэгч',
    path: '/dashboard/user',
    icon: icon('ic_user'),
  },
  {
    title: 'SKU',
    path: '/dashboard/products',
    icon: icon('ic_analytics'),
  },
  {
    title: 'Нэвтрэх',
    path: '/login',
    icon: icon('ic_lock'),
  },
  {
    title: 'Not found',
    path: '/404',
    icon: icon('ic_disabled'),
  },
];

export default navConfig;
