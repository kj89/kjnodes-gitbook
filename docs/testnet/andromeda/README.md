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
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:47656,2e6164a7c45c1840494af5db9bc54aacc39a065e@85.239.233.241:26656,457f5dbefe8b588c89d0892dcfff2a81d3e5cd74@45.133.216.14:26656,a4d291d17d8e74979e7db5a1e936269835e802af@194.165.59.78:26656,6006190d5a3a9686bbcce26abc79c7f3f868f43a@37.252.184.230:26656,bd323d2c7ce260b831d20923d390e4a1623f32c4@213.239.215.195:20095,385bda41dc8ce86d0dd4c99d3cf371ca8fccfeb6@135.125.189.131:20095,1d94f397352dc20be4b56e4bfd9305649cbac778@65.108.232.150:20095,443a51f595c9ca16273ca6146db1375e4223a91f@172.93.110.154:26656,7ac17e470c16814be55aa02a1611b23a3fba3097@75.119.141.16:26656,03603fb96ded3aabe7451efad31fb8d0c523a0ee@146.19.75.97:26656,9230896c5f22a363eed1c3bd3ed8068134b1dedd@110.168.55.28:26656,b6dd58949a8b9c03349bdbec8aeeccd5e0d39283@31.220.74.50:26656,69e89a5169fef99ed1b72dadd4f5c7b801616c88@142.132.209.236:21256,27e4aeaf8ef79a25904cd1042cf25ac6a1a0e7e5@103.180.28.220:26656,704e605f9bd65912d8c65a58f955601c31188548@65.21.203.204:19656,0a9c34419331688b0b40d50fddbee286927602cb@5.78.79.97:26656,7649ae1ea0dd5f640ac7dd7632a0866cf65e3aa4@31.220.90.78:26656,46350cf66cde21dfa16b92c2fb4a9d531de7c746@65.108.54.86:26656,dd1ae987d761a59f81a66fc4730f9d21b9aefdbd@146.0.36.92:26656,d68d0ce3a3959f09ea935cffbf1cd282dcfec401@27.72.126.82:26656,1eac9d697c4ee79b5cd1b706a7b6a2ca500d7361@93.170.47.119:26656,18296589a77b09df6c75559c84815f71fb7add9e@194.163.147.189:26656,c089b582977f015b7ee1ff357a9ca7c07f6341ca@135.181.221.186:31656,e8f8c97c65b3e65797eca3489de7c1682e85d4df@78.25.143.46:47656,f1d30c5f2d5882823317718eb4455f87ae846d0a@85.239.235.235:30656,62f7aaafd73816bdaf685a6270541c1d1f8162ad@155.133.27.170:26656,5cfce64114f98e29878567bdd1adbebe18670fc6@65.108.231.124:30656,3b998a882d8d9bcb2869eef988af86254e0e9602@89.116.29.20:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
