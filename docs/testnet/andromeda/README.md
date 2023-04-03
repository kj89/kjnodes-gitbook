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
peers="99cebda3a65a35b9a6a8bef774c8b92c1e548aa5@65.108.226.26:36656,e2efe3e1d7e0ed2e5b6a1b384c47f745e9f205ac@65.108.141.109:31656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:47656,a4d291d17d8e74979e7db5a1e936269835e802af@194.165.59.78:26656,6006190d5a3a9686bbcce26abc79c7f3f868f43a@37.252.184.230:26656,bd323d2c7ce260b831d20923d390e4a1623f32c4@213.239.215.195:20095,704e605f9bd65912d8c65a58f955601c31188548@65.21.203.204:19656,385bda41dc8ce86d0dd4c99d3cf371ca8fccfeb6@135.125.189.131:20095,443a51f595c9ca16273ca6146db1375e4223a91f@172.93.110.154:26656,1d94f397352dc20be4b56e4bfd9305649cbac778@65.108.232.150:20095,cdd5f44252e54bf8ebc4d35f10f1dbc40bb94128@194.163.134.227:26656,457f5dbefe8b588c89d0892dcfff2a81d3e5cd74@45.133.216.14:26656,dd1ae987d761a59f81a66fc4730f9d21b9aefdbd@146.0.36.92:26656,72bba2142c9cada7e4b8e861fb79e8a66e345d99@95.217.236.79:50656,69e89a5169fef99ed1b72dadd4f5c7b801616c88@142.132.209.236:21256,9230896c5f22a363eed1c3bd3ed8068134b1dedd@110.168.55.28:26656,0a9c34419331688b0b40d50fddbee286927602cb@5.78.79.97:26656,faca6fc28aa3aede1a90b89e39fa62d9fb424133@65.109.81.119:10656,9e14886f7a34c73e65eafb209a9215e2848e9e76@65.108.41.172:29456,0cc98f28ed826b3b43d2c88deb214ff01b36f6ce@159.69.126.18:15656,3d25f45062b5f3f49a87d38300ca0f657a9c853f@84.252.159.238:02656,d68d0ce3a3959f09ea935cffbf1cd282dcfec401@27.72.126.82:26656,b32691e0fbe837b45f645c1e4d30c96731b6e0c9@135.181.248.87:11656,b6dd58949a8b9c03349bdbec8aeeccd5e0d39283@31.220.74.50:26656,c089b582977f015b7ee1ff357a9ca7c07f6341ca@135.181.221.186:31656,27e4aeaf8ef79a25904cd1042cf25ac6a1a0e7e5@103.180.28.220:26656,3b998a882d8d9bcb2869eef988af86254e0e9602@89.116.29.20:26656,cc1c2cd585792d81a041e9098e36814dc8d1e6ae@213.239.207.165:28756,2e6164a7c45c1840494af5db9bc54aacc39a065e@85.239.233.241:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
