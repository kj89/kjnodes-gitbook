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
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:47656,3f9594221efe3e9cd4d0de31f71993fc0f12bf01@65.21.245.252:26656,f1d30c5f2d5882823317718eb4455f87ae846d0a@85.239.235.235:30656,27e4aeaf8ef79a25904cd1042cf25ac6a1a0e7e5@103.180.28.220:26656,a4d291d17d8e74979e7db5a1e936269835e802af@194.165.59.78:26656,bd323d2c7ce260b831d20923d390e4a1623f32c4@213.239.215.195:20095,704e605f9bd65912d8c65a58f955601c31188548@65.21.203.204:19656,385bda41dc8ce86d0dd4c99d3cf371ca8fccfeb6@135.125.189.131:20095,9d443f465ad66671d109142715e62ef8039cf0f8@161.97.85.248:26656,b6dd58949a8b9c03349bdbec8aeeccd5e0d39283@31.220.74.50:26656,443a51f595c9ca16273ca6146db1375e4223a91f@172.93.110.154:26656,1d94f397352dc20be4b56e4bfd9305649cbac778@65.108.232.150:20095,ef6ec2cf74e157e3c6056c0469f3ede08b418ec7@144.76.164.139:15656,03603fb96ded3aabe7451efad31fb8d0c523a0ee@146.19.75.97:26656,9230896c5f22a363eed1c3bd3ed8068134b1dedd@110.168.55.28:26656,d68d0ce3a3959f09ea935cffbf1cd282dcfec401@27.72.126.82:26656,133c61b0eb650e006908dd7a0066312337fe5e2c@31.220.73.35:26656,1b88dc10b14e01ef05a6c0721ce0cdd884746327@162.55.50.101:26656,c45d01b216a7f24a06448a47b6cf19a42e74c29b@65.21.170.3:32656,05b853c6022c51b2065665e66876e27aee9fed59@149.102.140.189:26656,6ea58e34e8abcfade1bf54d47cd2e2eddfd44495@143.198.129.53:47656,6d59b44efa40c4a03a24bf598b6cd662e8003655@135.181.96.66:26656,19ce9d4dcb2531e84280f5f42882e1a3623ab311@155.133.22.19:46656,dc5a74a53861ac287a1184a5688b1b466fe88836@34.165.27.178:26656,e61f287d51edab6f6dbe00a8b804614443ee6f82@80.85.242.117:26656,f3d598517ea86c08236b53882338b0b5e1d0f0e8@213.239.207.175:42656,5d076eccdbd1ae1835131be8e20b756e779c5bac@158.220.110.42:26656,6ef441d08cdb54b9f058884509ec65349976d73d@178.172.212.167:26656,32e94653d765d9a43eb9c7a97d752dd96b2a50d6@213.247.154.10:26656,20373ec71cffdb678099ca411fb862537f264791@178.172.212.135:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
