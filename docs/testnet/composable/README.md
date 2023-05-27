# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/composable.png" alt=""><figcaption></figcaption></figure>

The complete infrastructure for cross-chain smart  contracts, applications, and modular functionality.

**Chain ID**: banksy-testnet-2 | **Latest Version Tag**: v2.3.3-testnet2fork | **Wasm**: OFF

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
peers="c94f2c7161b02d55a62680c81998720dcbca6f60@109.236.86.96:15956,17ef33af803d45dff5eb164c655ea3aa4b4fa147@75.119.135.34:15656,fb195038778f02f9dfbfbad1cb2166dfd1caa142@65.21.200.161:15956,234fa34c415ebd65ede285f4098dcd6e762b0882@65.108.230.113:21206,56d356813115fc8f22450379b095b3e59290fba5@65.109.48.181:31656,2ca32b1aba0208008738ddefe44d5239bef2e894@95.217.144.107:22256,fe82bb3e15e4cee715f47a9ccb925134b9131669@46.4.213.193:26656,d14707d7abaeb27c040210d5343bf4141e29f513@65.108.13.154:37656,e6aa2a81f4b48b99d4d3f2ecd7739596af56d34d@148.113.143.196:26656,8859e665f2eca25da78aaf4d2e541407885b08d8@5.78.72.11:26656,156d57dfe94634eaba1c30f9ec2ce5ccee8410e1@65.21.88.12:2000,5070c358e90f8005b2049ff2e6d8e95adeb9bdd3@144.76.182.73:40656,367de894f877be9a9592f9d506c3082798b603e9@148.251.82.189:40656,d9b5a5910c1cf6b52f79aae4cf97dd83086dfc25@65.108.229.93:27656,7521d65a4102259fa26816383fea2f8f21a3b1ea@65.109.116.21:11154,872c8a78a17a24d6f44e1126c46ef52069c7bb18@65.109.80.150:2630,c4a216e6c01859509ffd8a94deee39a27fba525a@51.89.232.234:26656,f5fe55ea62334c68d08e6565794fe5c472936bf8@95.217.57.232:56656,5c2a752c9b1952dbed075c56c600c3a79b58c395@185.16.39.172:26976,eba3bc4613f3dac61201374ce09bee1fad00dc54@51.91.219.141:44003,945e8384ea51c5c6f7b9a90df8d8da120516d897@65.21.225.10:47656,7fc16efbb3e56d81245a0828198d580b3f246f58@51.91.30.173:3000,a39973a3ea8e5d9228c20e1c2a83f946fe1fb342@51.250.4.215:36656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15956,97ef8c9bc1b4d38088f453709b2d5bf06a19ebe6@95.216.14.45:26656,d850d1525f38622c2e8ea97a2ff91c63f8c8669c@193.26.159.34:12656,20f2608c9bc262df91d96027e1d5054ddee9c86c@142.132.209.236:22256,76065204ea3c9dbe8a722960b077b0ce62d05164@65.109.82.112:22656,0d533334454f9b95b01cb53c2704c7d48f19806c@71.236.119.108:41656,a9f62bf2505ba9dee4503ad0c383ad31a787d75a@212.23.222.6:11156"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.banksy/config/config.toml
```
