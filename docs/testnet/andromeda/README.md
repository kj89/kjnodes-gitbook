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
peers="c089b582977f015b7ee1ff357a9ca7c07f6341ca@135.181.221.186:31656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:47656,a4d291d17d8e74979e7db5a1e936269835e802af@194.165.59.78:26656,704e605f9bd65912d8c65a58f955601c31188548@65.21.203.204:19656,385bda41dc8ce86d0dd4c99d3cf371ca8fccfeb6@135.125.189.131:20095,443a51f595c9ca16273ca6146db1375e4223a91f@172.93.110.154:26656,1d94f397352dc20be4b56e4bfd9305649cbac778@65.108.232.150:20095,b6dd58949a8b9c03349bdbec8aeeccd5e0d39283@31.220.74.50:26656,93e418796bf3b5d8cd319983269c99db83cb2ba6@5.161.78.48:16656,247f3c2bed475978af238d97be68226c1f084180@88.99.164.158:4376,f1d30c5f2d5882823317718eb4455f87ae846d0a@85.239.235.235:30656,d68d0ce3a3959f09ea935cffbf1cd282dcfec401@27.72.126.82:26656,27e4aeaf8ef79a25904cd1042cf25ac6a1a0e7e5@103.180.28.220:26656,05b853c6022c51b2065665e66876e27aee9fed59@149.102.140.189:26656,41681200a0e60e9477181db813e1894684020378@194.233.92.77:26656,1b88dc10b14e01ef05a6c0721ce0cdd884746327@162.55.50.101:26656,bd323d2c7ce260b831d20923d390e4a1623f32c4@213.239.215.195:20095,e61f287d51edab6f6dbe00a8b804614443ee6f82@80.85.242.117:26656,95e8225c5b8a21c1fecd411f37c75f5515de1891@185.197.251.203:26656,7ac17e470c16814be55aa02a1611b23a3fba3097@75.119.141.16:26656,9230896c5f22a363eed1c3bd3ed8068134b1dedd@110.168.55.28:26656,6d59b44efa40c4a03a24bf598b6cd662e8003655@135.181.96.66:26656,ef6ec2cf74e157e3c6056c0469f3ede08b418ec7@144.76.164.139:15656,5d076eccdbd1ae1835131be8e20b756e779c5bac@158.220.110.42:26656,9d443f465ad66671d109142715e62ef8039cf0f8@161.97.85.248:26656,9939a8f08849b1d77b1bd5f5033d6ce9ff7a20f5@49.12.234.38:20656,debdccc98a2f6ed72561d7866381003903197935@144.126.142.78:29656,39429a15338825ea4fa6b310a7b12505e45b95d0@213.133.100.172:26858,5cfce64114f98e29878567bdd1adbebe18670fc6@65.108.231.124:30656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
