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
peers="8083dd301a7189284bf5b8d40c4cf239360d653a@5.9.122.49:26656,54188a9dea5ded1d891aa6c3c0e2a403322b1707@178.54.78.180:16656,6d59b44efa40c4a03a24bf598b6cd662e8003655@135.181.96.66:26656,00171178f5d8b22d1a3396d9388adbb8ec1c0541@38.242.208.162:36656,a4d291d17d8e74979e7db5a1e936269835e802af@194.165.59.78:26656,62f7aaafd73816bdaf685a6270541c1d1f8162ad@155.133.27.170:26656,1141119a7d248cc19b31b18d56162a365954deb9@45.132.106.149:26656,1d94f397352dc20be4b56e4bfd9305649cbac778@65.108.232.150:20095,05d3613dfb738ff22d0ea974bd0d1353ecdc6231@65.108.101.124:26656,385bda41dc8ce86d0dd4c99d3cf371ca8fccfeb6@135.125.189.131:20095,eec703fc2d5e7c1bbd81726a9e029dbb8b6221b5@178.250.247.119:26656,d3c2ce714e2c803d8686a0101711bf7164f844be@62.171.146.21:26656,9230896c5f22a363eed1c3bd3ed8068134b1dedd@124.120.12.196:26656,38a626dfc05c0d9756098349ce8ccd532496d6a2@65.108.206.118:61456,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:47656,00c49b6c8f0613bda77f27bf5072e4a000ace2b7@89.252.21.37:60556,443a51f595c9ca16273ca6146db1375e4223a91f@172.93.110.154:26656,7ac17e470c16814be55aa02a1611b23a3fba3097@75.119.141.16:26656,5cfce64114f98e29878567bdd1adbebe18670fc6@65.108.231.124:30656,27e4aeaf8ef79a25904cd1042cf25ac6a1a0e7e5@103.180.28.220:26656,bd323d2c7ce260b831d20923d390e4a1623f32c4@213.239.215.195:20095,24971494b3a2045d26b111c85e1ea6baf15fece3@89.169.46.109:26656,3b998a882d8d9bcb2869eef988af86254e0e9602@89.116.29.20:26656,c98370542e13e0d5b1aeb742fef9e7e717f04ff4@194.34.232.150:47656,b6dd58949a8b9c03349bdbec8aeeccd5e0d39283@31.220.74.50:26656,05b853c6022c51b2065665e66876e27aee9fed59@149.102.140.189:26656,6006190d5a3a9686bbcce26abc79c7f3f868f43a@37.252.184.230:26656,c4bb11ae43f4db7b8eef312a3c38861d236eb660@91.201.113.194:26656,e61f287d51edab6f6dbe00a8b804614443ee6f82@80.85.242.117:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
