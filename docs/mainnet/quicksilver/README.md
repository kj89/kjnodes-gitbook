# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/quicksilver.png" alt=""><figcaption></figcaption></figure>

Quicksilver is a permissionless, sovereign Cosmos SDK zone providing liquid staking for the entire Cosmos Ecosystem.

**Chain ID**: quicksilver-2 | **Latest Version Tag**: v1.2.9-hotfix.0 | **Wasm**: OFF

[Website](https://quicksilver.zone) | [Discord](https://discord.gg/quicksilverprotocol) | [Twitter](https://twitter.com/quicksilverzone)

[![Stake with kjnodes](https://i.ibb.co/cr44Q8j/button-stake-with-kjnodes.png)](https://restake.app/quicksilver/quickvaloper1fqfgpwdngmmay6ah7mg9y4k7ayykpzu6l3ht2m)

Subscribe to our free [🤖 Mainnet Proposal Bot](https://t.me/kjnodes_proposal_bot) to never miss upcoming proposals

## Restake

[Restake with kjnodes](https://restake.app/quicksilver/quickvaloper1fqfgpwdngmmay6ah7mg9y4k7ayykpzu6l3ht2m) (every 5 minutes)
## Chain explorer
[https://explorer.kjnodes.com/quicksilver](https://explorer.kjnodes.com/quicksilver)

## Public endpoints

* api: [https://quicksilver.api.kjnodes.com](https://quicksilver.api.kjnodes.com)
* rpc: [https://quicksilver.rpc.kjnodes.com](https://quicksilver.rpc.kjnodes.com)
* grpc: quicksilver.grpc.kjnodes.com:11090

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@quicksilver.rpc.kjnodes.com:11656
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@quicksilver.rpc.kjnodes.com:11659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/quicksilver/addrbook.json > $HOME/.quicksilverd/config/addrbook.json
```

**live-peers** (30)
```bash
peers="51070ba609ede6d7eb334b8cf0ed585f2b1ab66b@135.181.76.99:26656,0a226e70ceb7a4123e66216d1ed83ef22ed8a187@185.119.118.118:2000,602700ce2ed57b2176514ec2ecbda079caa7a536@178.170.40.28:15620,6785dbb8a0138600e0e0faaa77baa375451b38bb@162.55.132.48:15620,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:11656,625eeb91fcc6242798f53426540825e5b37c7670@185.144.99.16:36656,9bd2b7e39fb0d823402f22c90e3000fdf3cd05bf@88.99.104.180:26656,e3dd956ac4081ba42ae3d038edd6d80ddf092751@198.199.90.99:26656,4de2811fd20d33110daf62223975beccecbe55a0@15.235.114.195:26656,b4bcce87121963e1e97619dc135f2eb1a9fd5dfc@88.198.32.17:36656,ebafaa0d0087ecfc785b095d6a91a67a12eecd80@5.9.100.25:26656,e726816f42831689eab9378d5d577f1d06d25716@176.9.188.21:26656,149a25417349d70f5e5127a5eb634dbfaf6e6c3a@142.165.207.19:56656,ae353518e6009eb48d80ccf6a006a9644e9dd309@146.19.24.101:26656,ba52d6744d89cf66cf29d7663a21e1299d0f6744@74.80.183.130:26654,3bd708547317e9efd8d63d8a51c5bc32d11f4840@138.201.32.103:26056,f73ee3d2450f41bcf1b2975552cdf60a118a64c9@46.4.50.247:11656,f736b49c260e11d3f81a5d99814eaeda396c1597@18.138.35.164:26656,161f453c9ff27f3120ec5078f56b505316fbc720@65.108.6.45:61156,0ad45ecd219b9151ac17951dc1cd6303bcda2b58@65.109.106.169:26656,cdd8e0e425f107d249389a5e4cea3494185d4a3a@193.70.45.106:11156,c3ec2daba16e457ca5117079f34ff49e99e7572d@65.109.94.221:35656,c8b01e6700d048b1aae34d76f5c56511b2a90ab1@57.128.133.24:26656,995fcd08f3423266338effe441804a5490a728a7@37.59.21.96:11156,e8a9be589ae825aa4368c6a00b50b7031d5de58b@65.108.78.107:21609,26d23125db7493486dc9931b4181425d725e4ac6@65.109.55.186:20656,5f0c0411e34e1c7d0b9c53749d90a923b5e8c625@65.21.133.125:35656,b00a1e8869d0a8327f12f12d6b63bacf15527525@213.239.207.175:32656,3b3c0037090a1b5ef9f7ac58ff79f33dffdd188a@142.132.253.112:15656,cbc2c7a7cd39750abee0dcd5dd2832feddbde20e@50.21.173.76:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.quicksilverd/config/config.toml
```
