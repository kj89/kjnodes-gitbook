# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/andromeda.png" alt=""><figcaption></figcaption></figure>

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

**live-peers** (28)
```bash
peers="94fdba93b79d27701896d65d8e60155e06326532@65.109.63.110:15656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:47656,c89e274523cec4a7445afaff1ab35029b090ff5b@65.109.116.204:20156,385bda41dc8ce86d0dd4c99d3cf371ca8fccfeb6@135.125.189.131:20095,443a51f595c9ca16273ca6146db1375e4223a91f@172.93.110.154:26656,9e14886f7a34c73e65eafb209a9215e2848e9e76@65.108.41.172:29456,05d3613dfb738ff22d0ea974bd0d1353ecdc6231@65.108.101.124:26656,f17030edb4e4ec7143c3e3bbbfaeee3dd1a619f2@194.34.232.224:56656,1141119a7d248cc19b31b18d56162a365954deb9@45.132.106.149:26656,ef8045e2922cf856b73f5fa5efdb79f925204ccf@65.109.117.159:15656,05b853c6022c51b2065665e66876e27aee9fed59@149.102.140.189:26656,72bba2142c9cada7e4b8e861fb79e8a66e345d99@95.217.236.79:50656,bd323d2c7ce260b831d20923d390e4a1623f32c4@213.239.215.195:20095,3b998a882d8d9bcb2869eef988af86254e0e9602@89.116.29.20:26656,9230896c5f22a363eed1c3bd3ed8068134b1dedd@124.120.21.244:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.140:27126,00171178f5d8b22d1a3396d9388adbb8ec1c0541@38.242.208.162:36656,7002fb6369cd13f8aa1520fd7a81e67a9adf2636@185.119.196.39:26656,0a9c34419331688b0b40d50fddbee286927602cb@5.78.79.97:26656,28ce2dfb6c76e0baa660ec647bafe4a3b88cb3b0@94.131.118.190:26656,38a626dfc05c0d9756098349ce8ccd532496d6a2@65.108.206.118:61456,b6dd58949a8b9c03349bdbec8aeeccd5e0d39283@31.220.74.50:26656,e61f287d51edab6f6dbe00a8b804614443ee6f82@80.85.242.117:26656,fb7db0edee4ee43c2c65a81fd33e201c758d93df@137.184.176.247:47656,7649ae1ea0dd5f640ac7dd7632a0866cf65e3aa4@31.220.90.78:26656,9c04d97cdd28df85495fc99997e4eec0d43c2b47@94.130.218.86:15656,af5384af4257fdff39a2ee2535a1b74c3e052cad@65.109.229.186:26656,155b0aea2daadbb77e9eb1fbb235d2d81f7467c9@104.248.135.127:47656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
