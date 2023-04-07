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
peers="161f453c9ff27f3120ec5078f56b505316fbc720@65.108.6.45:61156,1b569bf57da79df4f85d207a161a97626988af76@65.109.92.241:20026,c764a288f1d36e7ca2c953378bb4fd6a0eed4091@141.95.65.73:11156,c8b01e6700d048b1aae34d76f5c56511b2a90ab1@57.128.133.24:26656,e64a4e480a2971c339fa06a58293e8e060082ad5@185.16.36.134:26656,271419d3eb3878c902ebb0064490ad702d9d067f@144.76.145.150:26656,ff2055b198685f619897058a26776b9d1b73dc3c@178.63.184.129:26656,c05c72b90e5a3d80f67e9da884a3f97b884d8ac2@65.109.112.29:26656,0a226e70ceb7a4123e66216d1ed83ef22ed8a187@185.119.118.118:2000,ebafaa0d0087ecfc785b095d6a91a67a12eecd80@5.9.100.25:26656,e3dd956ac4081ba42ae3d038edd6d80ddf092751@198.199.90.99:26656,c3ec2daba16e457ca5117079f34ff49e99e7572d@65.109.94.221:35656,e726816f42831689eab9378d5d577f1d06d25716@176.9.188.21:26656,225a08945298003a397eb6a51854525948fd9a5b@162.55.245.149:2010,9f0770c748d9323223722faacd30262218287b40@65.108.238.102:11156,06230bbaabb6c9c6223275b57d8e10fc609ae7ba@51.89.7.184:26633,ebc272824924ea1a27ea3183dd0b9ba713494f83@195.3.220.136:27026,b71ddbe0702383c73128f759a910a6d55ccee3b6@46.4.112.18:11656,6785dbb8a0138600e0e0faaa77baa375451b38bb@162.55.132.48:15620,3bd708547317e9efd8d63d8a51c5bc32d11f4840@138.201.32.103:26056,ae353518e6009eb48d80ccf6a006a9644e9dd309@146.19.24.101:26656,28ebd43e8c888ed069165fa035e101ae6fd7955e@139.162.191.246:26656,bbb6a02a90ef98975525d9bd7137511e18edddc1@141.95.99.81:26656,4559f4c24037bfad4791b2a6d6d5c769a16cad53@65.109.92.79:15656,9bed2c944243fd3ee35a6e4e8da0956f61518603@65.109.19.176:26656,51070ba609ede6d7eb334b8cf0ed585f2b1ab66b@135.181.76.99:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:11656,3394976851c8a06002989572119925f6d839a980@51.195.234.250:26656,6f80fa3110d45fa7cf08fe7df94cf9f60da8ad4a@178.63.67.112:26656,602700ce2ed57b2176514ec2ecbda079caa7a536@178.170.40.28:15620"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.quicksilverd/config/config.toml
```
