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
peers="ef1cb5bff5b76957f02636a30d5d85d861a35dbe@65.109.92.240:21026,58fe3a7b075e7302f8b46b8171a0aa19ff4a427a@65.108.195.29:31126,914bed178748772d7578d119cb2dc89d5076b9f4@135.181.223.115:2390,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:11656,7b5fc2dfe1ca54840bd1ea7c332a7516d8ae772f@65.108.130.171:26656,ebc272824924ea1a27ea3183dd0b9ba713494f83@195.3.220.136:27026,6f80fa3110d45fa7cf08fe7df94cf9f60da8ad4a@178.63.67.112:26656,06230bbaabb6c9c6223275b57d8e10fc609ae7ba@51.89.7.184:26633,443ad7c991b2915b620673b10206c92e2b4040e0@173.67.177.120:26656,c3ec2daba16e457ca5117079f34ff49e99e7572d@65.109.94.221:35656,28ebd43e8c888ed069165fa035e101ae6fd7955e@139.162.191.246:26656,e3dd956ac4081ba42ae3d038edd6d80ddf092751@198.199.90.99:26656,c05c72b90e5a3d80f67e9da884a3f97b884d8ac2@65.109.112.29:26656,0a226e70ceb7a4123e66216d1ed83ef22ed8a187@185.119.118.118:2000,71f722098fc28c2f39026af58d539f387451ddb0@65.109.86.210:27656,225a08945298003a397eb6a51854525948fd9a5b@162.55.245.149:2010,2020c09ef7542899a4c55b382013c469122186d6@51.195.88.136:15620,e09b47db9c221a9d064069befcc471d949d2c28d@45.14.135.159:15620,640c718263c0805e0336c6c35a45edec4f11294f@65.109.32.174:26656,51070ba609ede6d7eb334b8cf0ed585f2b1ab66b@135.181.76.99:26656,c71c7b9374aa551836c6e3a5530b94d7525abebb@3.76.82.136:26656,3bd869c02bd787d7bcc3b7059364608fc4e44620@141.94.202.185:32306,3bd708547317e9efd8d63d8a51c5bc32d11f4840@138.201.32.103:26056,e726816f42831689eab9378d5d577f1d06d25716@176.9.188.21:26656,b71ddbe0702383c73128f759a910a6d55ccee3b6@46.4.112.18:11656,ebafaa0d0087ecfc785b095d6a91a67a12eecd80@5.9.100.25:26656,602700ce2ed57b2176514ec2ecbda079caa7a536@178.170.40.28:15620,6da58393fe484687bc5f3067a891717f0e7d0760@167.235.15.79:26656,be4ff5b09936e32d9a4f87f5a5118973160d58f2@78.47.214.204:26656,c8b01e6700d048b1aae34d76f5c56511b2a90ab1@57.128.133.24:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.quicksilverd/config/config.toml
```
