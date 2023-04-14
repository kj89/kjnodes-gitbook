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
peers="6053a39e67c6bae83430e354f53d99e160e4964b@65.109.28.177:28656,4559f4c24037bfad4791b2a6d6d5c769a16cad53@65.109.92.79:15656,bbb6a02a90ef98975525d9bd7137511e18edddc1@141.95.99.81:26656,271419d3eb3878c902ebb0064490ad702d9d067f@144.76.145.150:26656,ff2055b198685f619897058a26776b9d1b73dc3c@178.63.184.129:26656,185f80586290dcd53db67ebc2da1e146e291bcd6@148.251.13.186:11156,cdd8e0e425f107d249389a5e4cea3494185d4a3a@193.70.45.106:11156,71d1e3336f41475c3dfc247aa77a8842a24c369a@144.91.80.32:11656,602700ce2ed57b2176514ec2ecbda079caa7a536@178.170.40.28:15620,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:11656,cbc2c7a7cd39750abee0dcd5dd2832feddbde20e@50.21.173.76:26656,f73ee3d2450f41bcf1b2975552cdf60a118a64c9@46.4.50.247:11656,6785dbb8a0138600e0e0faaa77baa375451b38bb@162.55.132.48:15620,e726816f42831689eab9378d5d577f1d06d25716@176.9.188.21:26656,0a226e70ceb7a4123e66216d1ed83ef22ed8a187@185.119.118.118:2000,d057145a457f3e3565926d3b385acd366f117d18@65.109.52.178:26656,c3ec2daba16e457ca5117079f34ff49e99e7572d@65.109.94.221:35656,8a0740d4b70629c26022db7525132da0062bf42b@194.62.99.114:26656,072c61dee7f205b237aae0eca698aa4a0639d93e@95.214.54.28:26356,225a08945298003a397eb6a51854525948fd9a5b@162.55.245.149:2010,ef1cb5bff5b76957f02636a30d5d85d861a35dbe@65.109.92.240:21026,ae3700d3296524014ab3444767df682b46f0cb9e@51.195.234.250:26656,a4f29a68180d1a1c931b50e2438a63b0d45d6915@89.58.48.229:26656,7b5fc2dfe1ca54840bd1ea7c332a7516d8ae772f@65.108.130.171:26656,e09b47db9c221a9d064069befcc471d949d2c28d@45.14.135.159:15620,9f0770c748d9323223722faacd30262218287b40@65.108.238.102:11156,ce593f9bffc471ba4b980a435a3e2f8eaa5b464e@34.159.4.248:26656,c05c72b90e5a3d80f67e9da884a3f97b884d8ac2@65.109.112.29:26656,e64a4e480a2971c339fa06a58293e8e060082ad5@185.16.36.134:26656,9284eae41fd79b5f5862702ee00ba4ea55d49f44@5.181.190.161:27060"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.quicksilverd/config/config.toml
```
