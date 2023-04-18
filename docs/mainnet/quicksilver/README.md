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
peers="b71ddbe0702383c73128f759a910a6d55ccee3b6@46.4.112.18:11656,be4ff5b09936e32d9a4f87f5a5118973160d58f2@78.47.214.204:26656,5fa47201aa5208c30982b6f9d8ca44222d256fc5@51.91.70.90:48656,cdd8e0e425f107d249389a5e4cea3494185d4a3a@193.70.45.106:11156,ce593f9bffc471ba4b980a435a3e2f8eaa5b464e@34.89.247.21:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:11656,3b3c0037090a1b5ef9f7ac58ff79f33dffdd188a@142.132.253.112:15656,03b3e3093b6cd33fba9f00cea6c2a560f89c61d6@195.14.6.2:26656,225a08945298003a397eb6a51854525948fd9a5b@162.55.245.149:2010,8a0740d4b70629c26022db7525132da0062bf42b@194.62.99.114:26656,c3ec2daba16e457ca5117079f34ff49e99e7572d@65.109.94.221:35656,040c3f32308aa75fa0f4d3b1b7c88ab5d45058a9@65.109.19.176:26656,6785dbb8a0138600e0e0faaa77baa375451b38bb@162.55.132.48:15620,f73ee3d2450f41bcf1b2975552cdf60a118a64c9@46.4.50.247:11656,0865ef3e5a613f75f17a0092bd47e71d8c171124@51.222.44.116:15656,a4f29a68180d1a1c931b50e2438a63b0d45d6915@89.58.48.229:26656,ebc272824924ea1a27ea3183dd0b9ba713494f83@195.3.220.136:27026,ef1cb5bff5b76957f02636a30d5d85d861a35dbe@65.109.92.240:21026,e3dd956ac4081ba42ae3d038edd6d80ddf092751@198.199.90.99:26656,e726816f42831689eab9378d5d577f1d06d25716@176.9.188.21:26656,ce3837aa07eb0967c024d4c592f7c2730754bdd8@157.90.179.182:26656,9bd2b7e39fb0d823402f22c90e3000fdf3cd05bf@88.99.104.180:26656,a1f5e0b68f36091d5fc8f30aba914b6c191f21fa@65.108.128.201:11156,185f80586290dcd53db67ebc2da1e146e291bcd6@148.251.13.186:11156,ebafaa0d0087ecfc785b095d6a91a67a12eecd80@5.9.100.25:26656,602700ce2ed57b2176514ec2ecbda079caa7a536@178.170.40.28:15620,ce4e8f10525ace89748180bddbd52fda70b78295@135.181.60.184:11656,0ad45ecd219b9151ac17951dc1cd6303bcda2b58@65.109.106.169:26656,cbc2c7a7cd39750abee0dcd5dd2832feddbde20e@50.21.173.76:26656,ae44851a5d63d70382c1621bc7727db2a40d10d0@88.99.164.158:21026"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.quicksilverd/config/config.toml
```
