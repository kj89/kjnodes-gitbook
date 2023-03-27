# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/nois.png" width="150" alt=""><figcaption></figcaption></figure>

Nois Network aims to bring randomness (or noise)  to the Cosmos ecosystem by providing a safe and  secure entropy source and distributing randomness  in the form of random beacons to other Cosmos blockchains via IBC.

**Chain ID**: nois-testnet-004 | **Latest Version Tag**: v0.6.0 | **Wasm**: ON

[Website](https://nois.network) | [Discord](https://discord.gg/dHdpwtEb6F) | [Twitter](https://twitter.com/NoisNetwork)



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

**live-peers** (35)
```bash
peers="9904ddc3186ea1e85390b8753da0e84948c1cf63@168.119.120.76:26656,bfbd43dbfbcda81b6d63f47e211f9d8eb323811c@65.109.39.50:26656,55b593887e758eeb7c1c6e3f8ffd8b30eabd0069@65.108.82.62:26656,91f2416b553b819b904c7e2b7823af3a7885e4d2@65.108.158.51:26656,e2c0a70930d3df0ea6b274ae73b4982b96492de4@65.108.233.109:17356,f4ed6f6bdf086cbaab9bed20e4dfc1daf326e4fc@89.117.50.54:26656,72cd4222818d25da5206092c3efc2c0dd0ec34fe@161.97.96.91:36656,6a9899efea58941ea40339beaba736b074aa695b@65.109.92.148:36656,c122b9227ebfbb508224421c0740fce710b3ff27@185.209.223.64:14656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27096,2fd09098fe74fb45d1fe1d5aca190df6c9eeefd1@65.108.75.32:26656,30bf62128e21bd7b4e375a43654d04a69a2e06a4@65.21.104.61:26656,0845590c7b9ac5d3a9813d1e06dfdf76c49f5876@142.132.209.236:17356,d2b5b5030e670d4ab37c7fdadb97c25a9f6b7045@78.46.61.117:14656,f7c0a82105152107c0e516056d0672d01a3a8582@88.99.56.200:26656,12c80b97e746b47b7b753aad9f3d85edab279957@104.193.254.42:27656,4aa321d62f82c4c0910bb9eec7a75c81d0157ceb@65.109.92.241:26656,7b94b17a9eb14e1e263c20e4f395a4b0f0bc1978@192.95.30.128:26656,c5dca34ba3ca713e1ac92d1cce5bc2371430b4c2@65.109.81.119:27656,f8383eeefdb51aaf37f231aac6acf837d76afb97@45.63.104.164:26656,c971d1a5a18a8d781f5dccf13df9391cb4ffc282@65.108.225.158:17356,f2315b5ce33cb2d2e0e4098dbf593b23710e995f@38.242.221.64:30656,a87dc8b4e827a05fe5c46aea54999120c8252587@162.19.237.81:26656,c3a3c2ed1132cc3a2554f0f8c77a60a34e7d4205@109.123.251.49:26656,c89ccec23799848505e1ecf7d3a36cdbe9046273@65.109.90.162:17656,fa51a34d907a7680e0622f676d24709ebc148e00@162.19.31.150:55726,0e88031f79f4aa005b966324decba5ade4787efb@162.55.223.152:26656,8cdf4ff3bef7d4545eb973a04d8225ab3cf48209@65.109.167.137:26656,f9179f009a0351a51cde673929f751cc0ca4dfc3@95.217.2.24:26656,7bf392b33faa03a68c83c933623c84cdfbcb5a0e@178.63.8.245:60656,c86b0c3ffb4fa65b188ac68d2872a9d91559bce1@65.21.55.133:26656,725d819ede610c0f276e1393b2ae1b256ca3b62e@95.217.154.80:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:51656,c53187e34d66494bb5ec89445008fad4a8517c83@65.109.5.235:21656,a5406759c96a87cb3a047014697ae13189963784@54.39.128.229:26636"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.noisd/config/config.toml
```
