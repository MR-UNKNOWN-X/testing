/**
* Ultroid - UserBot
* Copyright (C) 2020 TeamUltroid
*
* This file is a part of < https://github.com/MR-UNKNOWN-X/testing/ >
* PLease read the GNU Affero General Public License in
* <https://www.github.com/MR-UNKNOWN-X/testing/blob/main/LICENSE/>.
**/

import { bot, logger as log } from './bot';
import { initHandlers } from './handlers';
import { initMiddleWares } from './middlewares';

(async () => {
    initMiddleWares();
    initHandlers();
    await bot.telegram.deleteWebhook({ drop_pending_updates: true });
    await bot.launch();
    await log(`@${bot.botInfo?.username} is running...`);
})();
