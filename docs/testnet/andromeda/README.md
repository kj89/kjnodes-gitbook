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
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:47656,03603fb96ded3aabe7451efad31fb8d0c523a0ee@146.19.75.97:26656,6d59b44efa40c4a03a24bf598b6cd662e8003655@135.181.96.66:26656,a4d291d17d8e74979e7db5a1e936269835e802af@194.165.59.78:26656,27e4aeaf8ef79a25904cd1042cf25ac6a1a0e7e5@103.180.28.220:26656,bd323d2c7ce260b831d20923d390e4a1623f32c4@213.239.215.195:20095,385bda41dc8ce86d0dd4c99d3cf371ca8fccfeb6@135.125.189.131:20095,7ac17e470c16814be55aa02a1611b23a3fba3097@75.119.141.16:26656,c06d5254e4ecb69ccae41feff4d75de2dd92154d@149.102.138.176:26656,0a9c34419331688b0b40d50fddbee286927602cb@5.78.79.97:26656,b6dd58949a8b9c03349bdbec8aeeccd5e0d39283@31.220.74.50:26656,443a51f595c9ca16273ca6146db1375e4223a91f@172.93.110.154:26656,1d94f397352dc20be4b56e4bfd9305649cbac778@65.108.232.150:20095,d68d0ce3a3959f09ea935cffbf1cd282dcfec401@27.72.126.82:26656,2e6164a7c45c1840494af5db9bc54aacc39a065e@85.239.233.241:26656,1b88dc10b14e01ef05a6c0721ce0cdd884746327@162.55.50.101:26656,c089b582977f015b7ee1ff357a9ca7c07f6341ca@135.181.221.186:31656,3d582d84bb59245ad4ca0eeb32836f71404439a6@185.87.252.7:16656,9230896c5f22a363eed1c3bd3ed8068134b1dedd@110.168.55.28:26656,c4bb11ae43f4db7b8eef312a3c38861d236eb660@91.201.113.194:26656,c5f6021d8da08ff53e90725c0c2a77f8d65f5e03@195.201.195.40:26656,05b853c6022c51b2065665e66876e27aee9fed59@149.102.140.189:26656,457f5dbefe8b588c89d0892dcfff2a81d3e5cd74@45.133.216.14:26656,f1d30c5f2d5882823317718eb4455f87ae846d0a@85.239.235.235:30656,704e605f9bd65912d8c65a58f955601c31188548@65.21.203.204:19656,c45d01b216a7f24a06448a47b6cf19a42e74c29b@65.21.170.3:32656,99cebda3a65a35b9a6a8bef774c8b92c1e548aa5@65.108.226.26:36656,8870aca1936673bb2068ed07fcadc6c46d3ec3a1@146.190.83.6:22656,5cfce64114f98e29878567bdd1adbebe18670fc6@65.108.231.124:30656,dff203d0633c98eea4a228c5e913f22236043d89@23.88.69.101:16656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
