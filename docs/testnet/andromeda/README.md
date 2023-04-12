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
peers="22b94bd7f1c90560c631743be8866c11ca7b0758@65.109.116.110:26656,b797fd11dddbcfbae28fb70cb5d881cc03ad4dcb@38.242.131.206:36656,27e4aeaf8ef79a25904cd1042cf25ac6a1a0e7e5@103.180.28.220:26656,bd323d2c7ce260b831d20923d390e4a1623f32c4@213.239.215.195:20095,385bda41dc8ce86d0dd4c99d3cf371ca8fccfeb6@135.125.189.131:20095,443a51f595c9ca16273ca6146db1375e4223a91f@172.93.110.154:26656,1d94f397352dc20be4b56e4bfd9305649cbac778@65.108.232.150:20095,93e418796bf3b5d8cd319983269c99db83cb2ba6@5.161.78.48:16656,05b853c6022c51b2065665e66876e27aee9fed59@149.102.140.189:26656,a5f70c6cbcf4dd17f68237d2b1fe3e34564cb1dd@80.76.43.138:26656,5d076eccdbd1ae1835131be8e20b756e779c5bac@158.220.110.42:26656,9230896c5f22a363eed1c3bd3ed8068134b1dedd@124.120.20.220:26656,b6dd58949a8b9c03349bdbec8aeeccd5e0d39283@31.220.74.50:26656,99cebda3a65a35b9a6a8bef774c8b92c1e548aa5@65.108.226.26:36656,6d59b44efa40c4a03a24bf598b6cd662e8003655@135.181.96.66:26656,52ebde00c016f5f139e57eeca41b1f681647d23f@109.123.242.208:26656,9e14886f7a34c73e65eafb209a9215e2848e9e76@65.108.41.172:29456,e61f287d51edab6f6dbe00a8b804614443ee6f82@80.85.242.117:26656,c089b582977f015b7ee1ff357a9ca7c07f6341ca@135.181.221.186:31656,8870aca1936673bb2068ed07fcadc6c46d3ec3a1@146.190.83.6:22656,9d443f465ad66671d109142715e62ef8039cf0f8@161.97.85.248:26656,409a6d2be0ccf67b23c4080cf58d4b3d77a2b4ec@65.109.146.219:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.140:27126,7ac17e470c16814be55aa02a1611b23a3fba3097@75.119.141.16:26656,a4d291d17d8e74979e7db5a1e936269835e802af@194.165.59.78:26656,3c12c6f3798d7c3df09645b879c66f7841165b5e@37.120.171.213:14656,7649ae1ea0dd5f640ac7dd7632a0866cf65e3aa4@31.220.90.78:26656,5cfce64114f98e29878567bdd1adbebe18670fc6@65.108.231.124:30656,815e9378b05a40e4a774223b55f5c6b8457a1c79@31.220.79.166:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:47656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
