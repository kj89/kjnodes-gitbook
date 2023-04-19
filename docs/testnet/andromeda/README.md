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

**live-peers** (25)
```bash
peers="9939a8f08849b1d77b1bd5f5033d6ce9ff7a20f5@49.12.234.38:20656,05b853c6022c51b2065665e66876e27aee9fed59@149.102.140.189:26656,a4d291d17d8e74979e7db5a1e936269835e802af@194.165.59.78:26656,e61f287d51edab6f6dbe00a8b804614443ee6f82@80.85.242.117:26656,385bda41dc8ce86d0dd4c99d3cf371ca8fccfeb6@135.125.189.131:20095,443a51f595c9ca16273ca6146db1375e4223a91f@172.93.110.154:26656,1d94f397352dc20be4b56e4bfd9305649cbac778@65.108.232.150:20095,05d3613dfb738ff22d0ea974bd0d1353ecdc6231@65.108.101.124:26656,bd323d2c7ce260b831d20923d390e4a1623f32c4@213.239.215.195:20095,6d59b44efa40c4a03a24bf598b6cd662e8003655@135.181.96.66:26656,00171178f5d8b22d1a3396d9388adbb8ec1c0541@38.242.208.162:36656,27e4aeaf8ef79a25904cd1042cf25ac6a1a0e7e5@103.180.28.220:26656,94fdba93b79d27701896d65d8e60155e06326532@65.109.63.110:15656,9230896c5f22a363eed1c3bd3ed8068134b1dedd@124.120.12.196:26656,00c49b6c8f0613bda77f27bf5072e4a000ace2b7@89.252.21.37:60556,b6dd58949a8b9c03349bdbec8aeeccd5e0d39283@31.220.74.50:26656,7469fd307adba5d8e782908ee01f080f3e554c48@185.154.13.19:26656,fcc2e92679fd0bf000dce1e18d23143cf21ebea2@135.181.92.180:26656,d68d0ce3a3959f09ea935cffbf1cd282dcfec401@27.72.126.82:26656,5cfce64114f98e29878567bdd1adbebe18670fc6@65.108.231.124:30656,0a9c34419331688b0b40d50fddbee286927602cb@5.78.79.97:26656,3d25f45062b5f3f49a87d38300ca0f657a9c853f@84.252.159.238:02656,ce3a765f7075f3f5aee80bca0c76ca7dbe235731@167.235.198.193:36656,20248068f368f5d1eda74646d2bfd1fcdaffb3e1@89.58.59.75:60656,6ef441d08cdb54b9f058884509ec65349976d73d@178.172.212.167:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
