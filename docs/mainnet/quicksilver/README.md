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
peers="6053a39e67c6bae83430e354f53d99e160e4964b@65.109.28.177:28656,6785dbb8a0138600e0e0faaa77baa375451b38bb@162.55.132.48:15620,225a08945298003a397eb6a51854525948fd9a5b@162.55.245.149:2010,072c61dee7f205b237aae0eca698aa4a0639d93e@95.214.54.28:26356,3a5d0b97feb595375c24665dcf17d793be129e8b@51.89.155.2:28656,4ff179ec503516c869e4104bc0af85e324deefb2@46.101.75.31:15656,ff2055b198685f619897058a26776b9d1b73dc3c@178.63.184.129:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:11656,c3ec2daba16e457ca5117079f34ff49e99e7572d@65.109.94.221:35656,f73ee3d2450f41bcf1b2975552cdf60a118a64c9@46.4.50.247:11656,e09b47db9c221a9d064069befcc471d949d2c28d@45.14.135.159:15620,0a226e70ceb7a4123e66216d1ed83ef22ed8a187@185.119.118.118:2000,c05c72b90e5a3d80f67e9da884a3f97b884d8ac2@65.109.112.29:26656,ebc272824924ea1a27ea3183dd0b9ba713494f83@195.3.220.136:27026,ec076ff33f2986d064b78602e2ccd2c925bf761e@161.97.82.203:26256,23ebde0a3711817f66fd82436b32f3935e0b47ac@51.75.125.8:26656,ef1cb5bff5b76957f02636a30d5d85d861a35dbe@65.109.92.240:21026,ebafaa0d0087ecfc785b095d6a91a67a12eecd80@5.9.100.25:26656,618e09601dd5abb2bd02de957982742e4c1975ab@195.14.6.2:26656,d057145a457f3e3565926d3b385acd366f117d18@65.109.52.178:26656,bdbb005129890e3b656841415b3b728d1e4529e6@176.9.155.98:26656,0dfdec8a3bba26ad4258d3fd67a8468c10c3109c@195.114.30.92:11656,e726816f42831689eab9378d5d577f1d06d25716@176.9.188.21:26656,602700ce2ed57b2176514ec2ecbda079caa7a536@178.170.40.28:15620,ae3700d3296524014ab3444767df682b46f0cb9e@51.195.234.250:26656,e64a4e480a2971c339fa06a58293e8e060082ad5@185.16.36.134:26656,b71ddbe0702383c73128f759a910a6d55ccee3b6@46.4.112.18:11656,a0352933c3a4e525ac1cd595400f3123fbd597f6@65.108.230.161:46656,e3dd956ac4081ba42ae3d038edd6d80ddf092751@198.199.90.99:26656,cbc2c7a7cd39750abee0dcd5dd2832feddbde20e@50.21.173.76:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.quicksilverd/config/config.toml
```
