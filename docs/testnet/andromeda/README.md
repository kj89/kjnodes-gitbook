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

**live-peers** (29)
```bash
peers="91fde61878d704917f882694b271b67a38865ddc@149.102.142.94:26656,3322611985d1c6df9fa8da141887eeb0c473ae41@95.217.164.130:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:47656,6d59b44efa40c4a03a24bf598b6cd662e8003655@135.181.96.66:26656,bd323d2c7ce260b831d20923d390e4a1623f32c4@213.239.215.195:20095,00171178f5d8b22d1a3396d9388adbb8ec1c0541@38.242.208.162:36656,385bda41dc8ce86d0dd4c99d3cf371ca8fccfeb6@135.125.189.131:20095,443a51f595c9ca16273ca6146db1375e4223a91f@172.93.110.154:26656,1d94f397352dc20be4b56e4bfd9305649cbac778@65.108.232.150:20095,9e14886f7a34c73e65eafb209a9215e2848e9e76@65.108.41.172:29456,a4d291d17d8e74979e7db5a1e936269835e802af@194.165.59.78:26656,9230896c5f22a363eed1c3bd3ed8068134b1dedd@124.120.12.196:26656,e61f287d51edab6f6dbe00a8b804614443ee6f82@80.85.242.117:26656,05d3613dfb738ff22d0ea974bd0d1353ecdc6231@65.108.101.124:26656,b6dd58949a8b9c03349bdbec8aeeccd5e0d39283@31.220.74.50:26656,df7cf95427701d6d00797042fb8548a7f8eeeb6e@172.104.159.69:55716,d68d0ce3a3959f09ea935cffbf1cd282dcfec401@27.72.126.82:26656,38a626dfc05c0d9756098349ce8ccd532496d6a2@65.108.206.118:61456,27e4aeaf8ef79a25904cd1042cf25ac6a1a0e7e5@103.180.28.220:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.140:27126,99cebda3a65a35b9a6a8bef774c8b92c1e548aa5@65.108.226.26:36656,5cfce64114f98e29878567bdd1adbebe18670fc6@65.108.231.124:30656,05b853c6022c51b2065665e66876e27aee9fed59@149.102.140.189:26656,717066f5726fb3cd7096f84911c7c8bfe5953e62@81.68.158.68:26656,5795a44b9e632d5f24c61fa09a434e487355d0a4@144.91.70.120:26656,0a9c34419331688b0b40d50fddbee286927602cb@5.78.79.97:26656,c089b582977f015b7ee1ff357a9ca7c07f6341ca@135.181.221.186:31656,ce3a765f7075f3f5aee80bca0c76ca7dbe235731@167.235.198.193:36656,3d25f45062b5f3f49a87d38300ca0f657a9c853f@84.252.159.238:02656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
