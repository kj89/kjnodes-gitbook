# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/andromeda.png" width="150" alt=""><figcaption></figcaption></figure>

Andromeda is an application platform layer that connects all  public blockchains in the Cosmos ecosystem. Through our vast  library of no-code smart contracts, users can harness the power of web3.

**Chain ID**: galileo-3 | **Latest Version Tag**: galileo-3-v1.1.0-beta1 | **Wasm**: ON

[Website](https://www.andromedaprotocol.io) | [Discord](https://discord.gg/wzM3kSN3sE) | [Twitter](https://twitter.com/andromedaprot)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/andromeda-testnet](https://explorer.kjnodes.com/andromeda-testnet)

## Public endpoints

* api: [https://andromeda-testnet.api.kjnodes.com](https://andromeda-testnet.api.kjnodes.com)
* rpc: [https://andromeda-testnet.rpc.kjnodes.com](https://andromeda-testnet.rpc.kjnodes.com)
* grpc: andromeda-testnet.grpc.kjnodes.com:47090

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@andromeda-testnet.rpc.kjnodes.com:47656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@andromeda-testnet.rpc.kjnodes.com:47659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/andromeda-testnet/addrbook.json > $HOME/.andromedad/config/addrbook.json
```

**live-peers** (30)
```bash
peers="e95899eb682e517d74449dd575073daf1a3266d5@135.181.208.169:27656,717066f5726fb3cd7096f84911c7c8bfe5953e62@81.68.158.68:26656,a14e423bd01f55bdc29c2eeac99aaa0398e94228@45.14.194.212:26656,a4d291d17d8e74979e7db5a1e936269835e802af@194.165.59.78:26656,00c49b6c8f0613bda77f27bf5072e4a000ace2b7@89.252.21.37:60556,00171178f5d8b22d1a3396d9388adbb8ec1c0541@38.242.208.162:36656,1d94f397352dc20be4b56e4bfd9305649cbac778@65.108.232.150:20095,05d3613dfb738ff22d0ea974bd0d1353ecdc6231@65.108.101.124:26656,94fdba93b79d27701896d65d8e60155e06326532@65.109.63.110:15656,99cebda3a65a35b9a6a8bef774c8b92c1e548aa5@65.108.226.26:36656,e61f287d51edab6f6dbe00a8b804614443ee6f82@80.85.242.117:26656,443a51f595c9ca16273ca6146db1375e4223a91f@172.93.110.154:26656,9230896c5f22a363eed1c3bd3ed8068134b1dedd@124.120.12.196:26656,b6dd58949a8b9c03349bdbec8aeeccd5e0d39283@31.220.74.50:26656,1141119a7d248cc19b31b18d56162a365954deb9@45.132.106.149:26656,385bda41dc8ce86d0dd4c99d3cf371ca8fccfeb6@135.125.189.131:20095,05b853c6022c51b2065665e66876e27aee9fed59@149.102.140.189:26656,7ac17e470c16814be55aa02a1611b23a3fba3097@75.119.141.16:26656,7c9e768cdaa68d5c27b49797284acbd9d0dd9716@79.137.248.65:26656,6d59b44efa40c4a03a24bf598b6cd662e8003655@135.181.96.66:26656,27e4aeaf8ef79a25904cd1042cf25ac6a1a0e7e5@103.180.28.220:26656,bd323d2c7ce260b831d20923d390e4a1623f32c4@213.239.215.195:20095,a53b5f21a2700c63d0b3a77d58835f0d9348d396@77.51.200.79:47656,9a40e9bb2f6d27ee36bb06908314c8052c923e94@80.76.43.138:26656,fb7db0edee4ee43c2c65a81fd33e201c758d93df@137.184.176.247:47656,eec703fc2d5e7c1bbd81726a9e029dbb8b6221b5@178.250.247.119:26656,7f32e615c80cefdd6b229cba300ef9a94287f3f3@178.250.243.84:26656,fd48e41b990c9ba2cdd3e2f5adf20b8ab237b328@1.15.110.177:26656,5cfce64114f98e29878567bdd1adbebe18670fc6@65.108.231.124:30656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:47656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
