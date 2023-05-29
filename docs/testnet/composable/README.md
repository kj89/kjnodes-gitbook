# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/composable.png" alt=""><figcaption></figcaption></figure>

The complete infrastructure for cross-chain smart  contracts, applications, and modular functionality.

**Chain ID**: banksy-testnet-3 | **Latest Version Tag**: v2.3.5 | **Wasm**: OFF

[Website](https://www.composable.finance) | [Discord](https://discord.gg/composable) | [Twitter](https://twitter.com/ComposableFin)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/composable-testnet](https://explorer.kjnodes.com/composable-testnet)

## Public endpoints

* api: [https://composable-testnet.api.kjnodes.com](https://composable-testnet.api.kjnodes.com)
* rpc: [https://composable-testnet.rpc.kjnodes.com](https://composable-testnet.rpc.kjnodes.com)
* grpc: composable-testnet.grpc.kjnodes.com:15990

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@composable-testnet.rpc.kjnodes.com:15956
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@composable-testnet.rpc.kjnodes.com:15959
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/composable-testnet/addrbook.json > $HOME/.banksy/config/addrbook.json
```

**live-peers** (30)
```bash
peers="0cc331c2ae0b907fef8911ec9f76e28b363af15e@176.9.2.2:40656,17ef33af803d45dff5eb164c655ea3aa4b4fa147@75.119.135.34:15656,b13a2ff87cf8ea23773f2f3d8ad5b96ae7eb0b0b@65.108.206.74:36656,7db3b7cf36369cc48db0e7b4f49f1bf4ea59d3ac@65.21.131.215:26616,4646414777f70d2635e794465c406ecf107b2beb@65.109.92.235:11106,156d57dfe94634eaba1c30f9ec2ce5ccee8410e1@65.21.88.12:2000,f5fe55ea62334c68d08e6565794fe5c472936bf8@95.217.57.232:56656,fe82bb3e15e4cee715f47a9ccb925134b9131669@46.4.213.193:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15956,e6aa2a81f4b48b99d4d3f2ecd7739596af56d34d@148.113.143.196:26656,2ca32b1aba0208008738ddefe44d5239bef2e894@95.217.144.107:22256,8859e665f2eca25da78aaf4d2e541407885b08d8@5.78.72.11:26656,7fc16efbb3e56d81245a0828198d580b3f246f58@51.91.30.173:3000,eba3bc4613f3dac61201374ce09bee1fad00dc54@51.91.219.141:44003,5c2a752c9b1952dbed075c56c600c3a79b58c395@185.16.39.172:26976,2b3ebaebbaaa6f43b0986a1e4a104a517ce64e6c@94.41.17.212:26656,a7fdc284303bc4a8e62782e2e8f81008ea45a2b2@5.161.104.182:26656,7521d65a4102259fa26816383fea2f8f21a3b1ea@65.109.116.21:11154,c16bc22759633af69b6f698840cf2ba4d80ad7f9@157.245.154.125:15956,d14707d7abaeb27c040210d5343bf4141e29f513@65.108.13.154:37656,96f7134bb4d8f2dce88d5509e5295fdc7d433c66@95.216.7.169:56656,20f2608c9bc262df91d96027e1d5054ddee9c86c@142.132.209.236:22256,c4c51318e4d9a863c019fb277e5ed6748590e5c6@66.45.233.110:26656,872c8a78a17a24d6f44e1126c46ef52069c7bb18@65.109.80.150:2630,d9b5a5910c1cf6b52f79aae4cf97dd83086dfc25@65.108.229.93:27656,059424904782adaf06f667a0cd568f6c6c60442c@65.109.27.75:16656,c4a216e6c01859509ffd8a94deee39a27fba525a@51.89.232.234:26656,ca034bb4163b0c612f3f96a9d086f393fcaa2fa2@88.99.199.86:40656,7bff2e43489a7acd09a38ab47c1f25ec24e24947@51.68.166.235:26656,5da0b9f8da1906a9282e62cd8056bded37332365@152.228.214.87:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.banksy/config/config.toml
```
