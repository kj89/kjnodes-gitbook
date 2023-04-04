# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/quicksilver.png" width="150" alt=""><figcaption></figcaption></figure>

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
peers="6785dbb8a0138600e0e0faaa77baa375451b38bb@162.55.132.48:15620,9bd2b7e39fb0d823402f22c90e3000fdf3cd05bf@88.99.104.180:26656,0a3860f9d3c27b34910fe8660240ae55699b55c2@84.244.95.245:26656,ae353518e6009eb48d80ccf6a006a9644e9dd309@146.19.24.101:26656,4de2811fd20d33110daf62223975beccecbe55a0@15.235.114.195:26656,1b569bf57da79df4f85d207a161a97626988af76@65.109.92.241:20026,ce593f9bffc471ba4b980a435a3e2f8eaa5b464e@34.141.1.82:26656,6f80fa3110d45fa7cf08fe7df94cf9f60da8ad4a@178.63.67.112:26656,e3dd956ac4081ba42ae3d038edd6d80ddf092751@198.199.90.99:26656,c3ec2daba16e457ca5117079f34ff49e99e7572d@65.109.94.221:35656,79b214369c8f52c2d33cf79fc1897677b24cf8cb@94.130.240.229:2000,ebafaa0d0087ecfc785b095d6a91a67a12eecd80@5.9.100.25:26656,bbb6a02a90ef98975525d9bd7137511e18edddc1@141.95.99.81:26656,e4dbb1c6075822390aa23885750b306e1a54f9b0@5.161.101.185:26656,063ff82334c29ab2ed5d9ddebd1953e7df984a58@35.213.176.209:26656,3bd708547317e9efd8d63d8a51c5bc32d11f4840@138.201.32.103:26056,cb6ae22e1e89d029c55f2cb400b0caa19cbe5523@172.111.52.50:32662,28ebd43e8c888ed069165fa035e101ae6fd7955e@139.162.191.246:26656,e726816f42831689eab9378d5d577f1d06d25716@176.9.188.21:26656,602700ce2ed57b2176514ec2ecbda079caa7a536@178.170.40.28:15620,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:11656,51070ba609ede6d7eb334b8cf0ed585f2b1ab66b@135.181.76.99:26656,0865ef3e5a613f75f17a0092bd47e71d8c171124@51.222.44.116:15656,d11e03ee30496ef827383d5dcbbc55e7b3171189@35.240.184.52:26656,3b3c0037090a1b5ef9f7ac58ff79f33dffdd188a@65.108.231.124:15656,3394976851c8a06002989572119925f6d839a980@51.195.234.250:26656,225a08945298003a397eb6a51854525948fd9a5b@162.55.245.149:2010,03b3e3093b6cd33fba9f00cea6c2a560f89c61d6@195.14.6.2:26656,443ad7c991b2915b620673b10206c92e2b4040e0@173.67.177.120:26656,06230bbaabb6c9c6223275b57d8e10fc609ae7ba@51.89.7.184:26633"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.quicksilverd/config/config.toml
```
