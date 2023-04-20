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

**live-peers** (31)
```bash
peers="161f453c9ff27f3120ec5078f56b505316fbc720@65.108.6.45:61156,89757803f40da51678451735445ad40d5b15e059@169.155.44.196:26656,71b753819eb653e99e6a825b80af20ca9bccb087@135.125.163.63:24666,841efbdd6cd5c7191b5ec849499dfd9d1ea6a931@23.88.69.22:28566,271419d3eb3878c902ebb0064490ad702d9d067f@144.76.145.150:26656,96b7605dbf13dbf0df2c3ac4f076397a9f351c6b@88.98.195.228:26656,602700ce2ed57b2176514ec2ecbda079caa7a536@178.170.40.28:15620,71f722098fc28c2f39026af58d539f387451ddb0@65.109.86.210:27656,e3dd956ac4081ba42ae3d038edd6d80ddf092751@198.199.90.99:26656,e726816f42831689eab9378d5d577f1d06d25716@176.9.188.21:26656,ef1cb5bff5b76957f02636a30d5d85d861a35dbe@65.109.92.240:21026,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:11656,f73ee3d2450f41bcf1b2975552cdf60a118a64c9@46.4.50.247:11656,ebc272824924ea1a27ea3183dd0b9ba713494f83@195.3.220.136:27026,c3ec2daba16e457ca5117079f34ff49e99e7572d@65.109.94.221:35656,8a0740d4b70629c26022db7525132da0062bf42b@194.62.99.114:26656,6785dbb8a0138600e0e0faaa77baa375451b38bb@162.55.132.48:15620,9bd2b7e39fb0d823402f22c90e3000fdf3cd05bf@88.99.104.180:26656,a4f29a68180d1a1c931b50e2438a63b0d45d6915@89.58.48.229:26656,225a08945298003a397eb6a51854525948fd9a5b@162.55.245.149:2010,03b3e3093b6cd33fba9f00cea6c2a560f89c61d6@195.14.6.2:26656,b00a1e8869d0a8327f12f12d6b63bacf15527525@213.239.207.175:32656,e64a4e480a2971c339fa06a58293e8e060082ad5@185.16.36.134:26656,08ab5be08f12754381c0fd088bb36d9d294f54c6@65.109.21.74:26656,ae44851a5d63d70382c1621bc7727db2a40d10d0@88.99.164.158:21026,a7d96dc929824613315dcc1c90fee119f28cc51f@169.155.168.83:26656,3308d9078fcca016fbd8dc8f3b19666326f41a6f@138.201.121.185:26672,185f80586290dcd53db67ebc2da1e146e291bcd6@148.251.13.186:11156,34047b39deae3110158c2bf7359e4a1b559dd8ca@159.89.171.207:26656,0ad45ecd219b9151ac17951dc1cd6303bcda2b58@65.109.106.169:26656,ff2055b198685f619897058a26776b9d1b73dc3c@178.63.184.129:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.quicksilverd/config/config.toml
```
