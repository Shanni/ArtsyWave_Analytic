import { Controller, Get } from '@nestjs/common';
import { AppService } from './app.service';

@Controller()
export class AppController {
  constructor(private readonly appService: AppService) {}

  @Get()
  getHello(): string {
    return this.appService.getHello();
  }

  // {
  //   "accessKey": "your-access-key",
  //   "context": {
  //     "assetId": "abcd1234",
  //     "userId": "user5678"
  //   },
  //   "timestamp": 1680530722502
  // }
}
