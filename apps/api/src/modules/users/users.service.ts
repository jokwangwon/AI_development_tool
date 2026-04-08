import { Injectable, NotFoundException } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { Repository } from 'typeorm';

import { UserEntity } from './entities/user.entity';
import { UserProgressEntity } from './entities/user-progress.entity';

@Injectable()
export class UsersService {
  constructor(
    @InjectRepository(UserEntity)
    private readonly userRepo: Repository<UserEntity>,
    @InjectRepository(UserProgressEntity)
    private readonly progressRepo: Repository<UserProgressEntity>,
  ) {}

  async findById(id: string): Promise<UserEntity> {
    const user = await this.userRepo.findOne({ where: { id } });
    if (!user) {
      throw new NotFoundException(`User ${id} not found`);
    }
    return user;
  }

  async findByEmail(email: string): Promise<UserEntity | null> {
    return this.userRepo.findOne({ where: { email } });
  }

  async create(input: {
    username: string;
    email: string;
    passwordHash: string;
  }): Promise<UserEntity> {
    const user = this.userRepo.create({ ...input, role: 'player' });
    return this.userRepo.save(user);
  }

  async getProgress(userId: string): Promise<UserProgressEntity[]> {
    return this.progressRepo.find({ where: { userId } });
  }
}
