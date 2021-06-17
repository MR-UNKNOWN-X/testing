/**
* Ultroid - UserBot
* Copyright (C) 2020 TeamUltroid
*
* This file is a part of < https://github.com/MR-UNKNOWN-X/testing/ >
* PLease read the GNU Affero General Public License in
* <https://www.github.com/MR-UNKNOWN-X/testing/blob/main/LICENSE/>.
**/

import { bot } from '../bot';

import Auth from './auth';
import Logger from './logger';

export const initMiddleWares = (): void => {
    bot.use(Logger);
    bot.use(Auth);
}