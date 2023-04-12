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
peers="f66bcec970aaaaa9ae33182802ac4bf87b3b20cd@84.46.254.82:26656,a4d291d17d8e74979e7db5a1e936269835e802af@194.165.59.78:26656,bd323d2c7ce260b831d20923d390e4a1623f32c4@213.239.215.195:20095,1d94f397352dc20be4b56e4bfd9305649cbac778@65.108.232.150:20095,6d59b44efa40c4a03a24bf598b6cd662e8003655@135.181.96.66:26656,27e4aeaf8ef79a25904cd1042cf25ac6a1a0e7e5@103.180.28.220:26656,385bda41dc8ce86d0dd4c99d3cf371ca8fccfeb6@135.125.189.131:20095,93e418796bf3b5d8cd319983269c99db83cb2ba6@5.161.78.48:16656,31930132bc99cf45a8802962df622928619a3001@207.154.241.168:26656,443a51f595c9ca16273ca6146db1375e4223a91f@172.93.110.154:26656,03603fb96ded3aabe7451efad31fb8d0c523a0ee@146.19.75.97:26656,9e14886f7a34c73e65eafb209a9215e2848e9e76@65.108.41.172:29456,b6dd58949a8b9c03349bdbec8aeeccd5e0d39283@31.220.74.50:26656,3b998a882d8d9bcb2869eef988af86254e0e9602@89.116.29.20:26656,52ebde00c016f5f139e57eeca41b1f681647d23f@109.123.242.208:26656,41681200a0e60e9477181db813e1894684020378@194.233.92.77:26656,5d076eccdbd1ae1835131be8e20b756e779c5bac@158.220.110.42:26656,815e9378b05a40e4a774223b55f5c6b8457a1c79@31.220.79.166:26656,086dd26d09ee6ff66307555cb9a25e0df76f377f@65.108.199.206:30656,9230896c5f22a363eed1c3bd3ed8068134b1dedd@124.120.20.220:26656,537e0302400604f7dd1b8e49c5660da311066610@199.175.98.104:26656,05b853c6022c51b2065665e66876e27aee9fed59@149.102.140.189:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:47656,99cebda3a65a35b9a6a8bef774c8b92c1e548aa5@65.108.226.26:36656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.140:27126,c089b582977f015b7ee1ff357a9ca7c07f6341ca@135.181.221.186:31656,ef6ec2cf74e157e3c6056c0469f3ede08b418ec7@144.76.164.139:15656,a5f70c6cbcf4dd17f68237d2b1fe3e34564cb1dd@80.76.43.138:26656,ce3a765f7075f3f5aee80bca0c76ca7dbe235731@167.235.198.193:36656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
