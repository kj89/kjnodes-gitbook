# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/nois.png" width="150" alt=""><figcaption></figcaption></figure>

Nois Network aims to bring randomness (or noise)  to the Cosmos ecosystem by providing a safe and  secure entropy source and distributing randomness  in the form of random beacons to other Cosmos blockchains via IBC.

**Chain ID**: nois-testnet-005 | **Latest Version Tag**: v1.0.0 | **Wasm**: ON

[Website](https://nois.network) | [Discord](https://discord.gg/dHdpwtEb6F) | [Twitter](https://twitter.com/NoisRNG)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/nois-testnet](https://explorer.kjnodes.com/nois-testnet)

## Public endpoints

* api: [https://nois-testnet.api.kjnodes.com](https://nois-testnet.api.kjnodes.com)
* rpc: [https://nois-testnet.rpc.kjnodes.com](https://nois-testnet.rpc.kjnodes.com)
* grpc: nois-testnet.grpc.kjnodes.com:51090

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@nois-testnet.rpc.kjnodes.com:51656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@nois-testnet.rpc.kjnodes.com:51659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/nois-testnet/addrbook.json > $HOME/.noisd/config/addrbook.json
```

**live-peers** (28)
```bash
peers="eff2a3659d8190f2e3f0556d9829288d29e63296@65.108.233.109:17356,457a8e8dcb3bef4d7a6fd7fcb3b97d1282ca029c@65.108.206.118:60856,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:51656,00c205b11dc2d2295749810722bb2e995a24c0c1@95.216.14.58:60656,80cb3138f2f951077c1e70686bb4f59e00cb1fad@135.181.18.112:55726,065caaf31329c02c0f8a32385e3c6a7f31e6b028@46.17.250.43:26656,50c9ac024633c1f0fc461958dafa15e6b2541ffd@79.143.183.91:26656,d50b83f0f8ce4125cdffb820f0836e58fa9b216a@85.173.112.154:20656,711a4b20ce63e3a69725d27c73145519a2a1b559@161.97.159.68:17356,ac4b7c231061e9c7ad3b69bcfd722bc878b3d8d4@162.55.103.44:26636,f7c0a82105152107c0e516056d0672d01a3a8582@88.99.56.200:26656,bfbd43dbfbcda81b6d63f47e211f9d8eb323811c@65.109.39.50:26656,65acf20f39df51e09027a2f204e359d57823a995@65.108.72.253:21656,35498a9c47c2901a097161cd5abc5bc758aa1b5c@38.242.158.85:51656,6d6164cd45c7c65ab76abd40f5ff683f72e7f50f@65.109.92.241:40136,2b265b12688ea801b11672a47b67bb55433ccf37@185.198.27.109:26656,aca79b135dd5f8498e3db6020dba3a1b557d644d@173.249.25.235:26656,136b148b3cae6ff4895e2039e11f221c7082ccd3@65.109.5.235:26656,a87dc8b4e827a05fe5c46aea54999120c8252587@162.19.237.81:26656,4af23e5bbb434e58082054a7d97b41b62cdb4a83@195.201.197.4:30656,4f4cbbb89deacb0a1f395050567e96bb70f4a1ff@142.132.152.46:41656,1e9f3c5da72edebe751b108aa52657b190c8991d@65.108.225.158:17356,40250630b11b62814410129ed5dc29221e141a2f@65.108.72.233:26156,2403cecea3dc5c6bcac9ff964095ac673fbc02ef@65.109.39.223:26636,d82a26ef1cebfa8a57e7b06a4310b800740c1c6d@144.76.30.36:15648,c9cb08536ae8c26d7e1a9461f7f8afd21e4e8784@95.217.196.105:26656,c60e7d9dffdc2b97e9d8b36861ff2e077c863482@65.108.2.41:60656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27286"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.noisd/config/config.toml
```
