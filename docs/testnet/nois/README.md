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

**live-peers** (29)
```bash
peers="a87dc8b4e827a05fe5c46aea54999120c8252587@162.19.237.81:26656,35498a9c47c2901a097161cd5abc5bc758aa1b5c@38.242.158.85:51656,6d6164cd45c7c65ab76abd40f5ff683f72e7f50f@65.109.92.241:40136,c60e7d9dffdc2b97e9d8b36861ff2e077c863482@65.108.2.41:60656,40250630b11b62814410129ed5dc29221e141a2f@65.108.72.233:26156,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27286,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:51656,5a2cf815580a74c31e722737b7f48747afba1137@95.216.197.76:26656,711a4b20ce63e3a69725d27c73145519a2a1b559@161.97.159.68:17356,262c94509b076029f04f1274536c5f458ec2463a@65.109.93.100:37656,80cb3138f2f951077c1e70686bb4f59e00cb1fad@135.181.18.112:55726,65acf20f39df51e09027a2f204e359d57823a995@65.108.72.253:21656,457a8e8dcb3bef4d7a6fd7fcb3b97d1282ca029c@65.108.206.118:60856,00c205b11dc2d2295749810722bb2e995a24c0c1@95.216.14.58:60656,4f4cbbb89deacb0a1f395050567e96bb70f4a1ff@142.132.152.46:41656,eff2a3659d8190f2e3f0556d9829288d29e63296@65.108.233.109:17356,e07c37d68a210ee89191543e64078c7b127aa6c4@65.108.78.101:30656,28a94656dd4ddde090d8dd3d89865db5b6cda0ce@95.217.58.111:26656,4af23e5bbb434e58082054a7d97b41b62cdb4a83@195.201.197.4:30656,4f581b36aac37da8766c9de4dc533b0740eb498d@38.242.222.52:26656,f7c0a82105152107c0e516056d0672d01a3a8582@88.99.56.200:26656,d82a26ef1cebfa8a57e7b06a4310b800740c1c6d@144.76.30.36:15648,1f1b67a13a6c9ef47cc21a9c71eeac1adc03e05b@176.9.10.239:26656,d30a17b9980314aadefd270f7ca9e4b810e94aca@5.166.240.95:51656,2b265b12688ea801b11672a47b67bb55433ccf37@185.198.27.109:26656,1e9f3c5da72edebe751b108aa52657b190c8991d@65.108.225.158:17356,d2d2dd4427bde768bbc2701536942b8f1174877e@65.108.77.106:26899,40fd0b54d6a096404421a36f29ae1e3779d2ae03@207.180.208.47:26656,bca6115a0d059d21781dcdc6bfa8149ec3961bb4@46.17.250.108:60556"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.noisd/config/config.toml
```
