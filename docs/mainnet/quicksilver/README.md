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
peers="ef1cb5bff5b76957f02636a30d5d85d861a35dbe@65.109.92.240:21026,ebafaa0d0087ecfc785b095d6a91a67a12eecd80@5.9.100.25:26656,0a3860f9d3c27b34910fe8660240ae55699b55c2@84.244.95.245:26656,71d1e3336f41475c3dfc247aa77a8842a24c369a@144.91.80.32:11656,96b7605dbf13dbf0df2c3ac4f076397a9f351c6b@88.98.195.228:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:11656,ff2055b198685f619897058a26776b9d1b73dc3c@178.63.184.129:26656,f73ee3d2450f41bcf1b2975552cdf60a118a64c9@46.4.50.247:11656,6785dbb8a0138600e0e0faaa77baa375451b38bb@162.55.132.48:15620,e3dd956ac4081ba42ae3d038edd6d80ddf092751@198.199.90.99:26656,602700ce2ed57b2176514ec2ecbda079caa7a536@178.170.40.28:15620,e726816f42831689eab9378d5d577f1d06d25716@176.9.188.21:26656,625eeb91fcc6242798f53426540825e5b37c7670@185.144.99.16:36656,225a08945298003a397eb6a51854525948fd9a5b@162.55.245.149:2010,0a226e70ceb7a4123e66216d1ed83ef22ed8a187@185.119.118.118:2000,ebc272824924ea1a27ea3183dd0b9ba713494f83@195.3.220.136:27026,c3ec2daba16e457ca5117079f34ff49e99e7572d@65.109.94.221:35656,3bd708547317e9efd8d63d8a51c5bc32d11f4840@138.201.32.103:26056,03b3e3093b6cd33fba9f00cea6c2a560f89c61d6@195.14.6.2:26656,e1a24aaba30a8ff21e52fed92b96b36156b52e80@51.161.208.88:26656,c05c72b90e5a3d80f67e9da884a3f97b884d8ac2@65.109.112.29:26656,6f80fa3110d45fa7cf08fe7df94cf9f60da8ad4a@178.63.67.112:26656,072c61dee7f205b237aae0eca698aa4a0639d93e@95.214.54.28:26356,765aa57477e21bf94d4c41dda643f297132a1178@51.195.234.250:26656,d057145a457f3e3565926d3b385acd366f117d18@65.109.52.178:26656,8a0740d4b70629c26022db7525132da0062bf42b@194.62.99.114:26656,cbc2c7a7cd39750abee0dcd5dd2832feddbde20e@50.21.173.76:26656,185f80586290dcd53db67ebc2da1e146e291bcd6@148.251.13.186:11156,6053a39e67c6bae83430e354f53d99e160e4964b@65.109.28.177:28656,3b3c0037090a1b5ef9f7ac58ff79f33dffdd188a@65.108.231.124:15656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.quicksilverd/config/config.toml
```
