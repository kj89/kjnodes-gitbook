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
peers="99cebda3a65a35b9a6a8bef774c8b92c1e548aa5@65.108.226.26:36656,3d25f45062b5f3f49a87d38300ca0f657a9c853f@84.252.159.238:02656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:47656,a4d291d17d8e74979e7db5a1e936269835e802af@194.165.59.78:26656,27e4aeaf8ef79a25904cd1042cf25ac6a1a0e7e5@103.180.28.220:26656,385bda41dc8ce86d0dd4c99d3cf371ca8fccfeb6@135.125.189.131:20095,443a51f595c9ca16273ca6146db1375e4223a91f@172.93.110.154:26656,1d94f397352dc20be4b56e4bfd9305649cbac778@65.108.232.150:20095,93e418796bf3b5d8cd319983269c99db83cb2ba6@5.161.78.48:16656,ce3a765f7075f3f5aee80bca0c76ca7dbe235731@167.235.198.193:36656,b6dd58949a8b9c03349bdbec8aeeccd5e0d39283@31.220.74.50:26656,d0ef5f5583ff0343ea41962f68010bff54caafde@212.90.121.45:30656,6d59b44efa40c4a03a24bf598b6cd662e8003655@135.181.96.66:26656,7c9e768cdaa68d5c27b49797284acbd9d0dd9716@79.137.248.65:26656,1c9d70cda1b46e8a33a39783e9af0ad8b5d876ac@65.109.85.225:3340,9230896c5f22a363eed1c3bd3ed8068134b1dedd@124.120.20.220:26656,e61f287d51edab6f6dbe00a8b804614443ee6f82@80.85.242.117:26656,c9333c13721f846a9dcfe2933ba618f84b6e7ac3@217.76.61.255:26656,f62f2dc135fb2cfd359459f702cc4b3f09f1c328@5.135.140.211:26656,5d076eccdbd1ae1835131be8e20b756e779c5bac@158.220.110.42:26656,7649ae1ea0dd5f640ac7dd7632a0866cf65e3aa4@31.220.90.78:26656,05b853c6022c51b2065665e66876e27aee9fed59@149.102.140.189:26656,960107661575543d797586726e8f1a3b889685c7@38.242.215.237:26656,bd323d2c7ce260b831d20923d390e4a1623f32c4@213.239.215.195:20095,f101cd993ea35add4e3b6b1492b6b1a2209a91c1@80.85.242.54:56656,1b88dc10b14e01ef05a6c0721ce0cdd884746327@162.55.50.101:26656,d68d0ce3a3959f09ea935cffbf1cd282dcfec401@27.72.126.82:26656,9939a8f08849b1d77b1bd5f5033d6ce9ff7a20f5@49.12.234.38:20656,53563e3ac27cd93b9ac1007be30de8c6b028ed21@65.21.153.86:26656,d408ae19e3d70f700b39128bcfb5350faa55d71d@65.109.28.226:01656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
