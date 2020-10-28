import { User } from './User';
import { Company } from './Company';
import {CustomMap} from './CustomMap';

const user = new User();
const company = new Company();
const customMap = new CustomMap('map');

console.log("Maps should be live now");

customMap.addMarker(user);
customMap.addMarker(company);