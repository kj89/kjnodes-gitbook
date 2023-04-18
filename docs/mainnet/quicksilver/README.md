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
peers="d5a9c9ae08f0d30e36c8f64eca046fc52b00561e@65.109.92.160:26656,f73b2b887e7d1c01a3d753db359a0058e634e767@65.108.201.154:2090,71f722098fc28c2f39026af58d539f387451ddb0@65.109.86.210:27656,cdd8e0e425f107d249389a5e4cea3494185d4a3a@193.70.45.106:11156,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:11656,f73ee3d2450f41bcf1b2975552cdf60a118a64c9@46.4.50.247:11656,3b3c0037090a1b5ef9f7ac58ff79f33dffdd188a@142.132.253.112:15656,e3dd956ac4081ba42ae3d038edd6d80ddf092751@198.199.90.99:26656,a4f29a68180d1a1c931b50e2438a63b0d45d6915@89.58.48.229:26656,c3ec2daba16e457ca5117079f34ff49e99e7572d@65.109.94.221:35656,6785dbb8a0138600e0e0faaa77baa375451b38bb@162.55.132.48:15620,ef1cb5bff5b76957f02636a30d5d85d861a35dbe@65.109.92.240:21026,ebafaa0d0087ecfc785b095d6a91a67a12eecd80@5.9.100.25:26656,ebc272824924ea1a27ea3183dd0b9ba713494f83@195.3.220.136:27026,4de2811fd20d33110daf62223975beccecbe55a0@15.235.114.195:26656,8a0740d4b70629c26022db7525132da0062bf42b@194.62.99.114:26656,0ad45ecd219b9151ac17951dc1cd6303bcda2b58@65.109.106.169:26656,e726816f42831689eab9378d5d577f1d06d25716@176.9.188.21:26656,225a08945298003a397eb6a51854525948fd9a5b@162.55.245.149:2010,602700ce2ed57b2176514ec2ecbda079caa7a536@178.170.40.28:15620,03b3e3093b6cd33fba9f00cea6c2a560f89c61d6@195.14.6.2:26656,96bd0e87a5e5b88e8ce637aa3c7aa4f4803b1d03@198.244.203.179:26656,c8b01e6700d048b1aae34d76f5c56511b2a90ab1@57.128.133.24:26656,b71ddbe0702383c73128f759a910a6d55ccee3b6@46.4.112.18:11656,bcbc620d23148bc8c42bfb21fc8bd6d1e779d83f@146.59.118.31:32182,7b5fc2dfe1ca54840bd1ea7c332a7516d8ae772f@65.108.130.171:26656,08ab5be08f12754381c0fd088bb36d9d294f54c6@65.109.21.74:26656,9bd2b7e39fb0d823402f22c90e3000fdf3cd05bf@88.99.104.180:26656,0865ef3e5a613f75f17a0092bd47e71d8c171124@51.222.44.116:15656,cbc2c7a7cd39750abee0dcd5dd2832feddbde20e@50.21.173.76:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.quicksilverd/config/config.toml
```
