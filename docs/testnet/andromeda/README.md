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
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:47656,9230896c5f22a363eed1c3bd3ed8068134b1dedd@124.120.12.196:26656,e61f287d51edab6f6dbe00a8b804614443ee6f82@80.85.242.117:26656,bd323d2c7ce260b831d20923d390e4a1623f32c4@213.239.215.195:20095,385bda41dc8ce86d0dd4c99d3cf371ca8fccfeb6@135.125.189.131:20095,443a51f595c9ca16273ca6146db1375e4223a91f@172.93.110.154:26656,1d94f397352dc20be4b56e4bfd9305649cbac778@65.108.232.150:20095,9e14886f7a34c73e65eafb209a9215e2848e9e76@65.108.41.172:29456,05d3613dfb738ff22d0ea974bd0d1353ecdc6231@65.108.101.124:26656,32e94653d765d9a43eb9c7a97d752dd96b2a50d6@213.247.154.10:26656,00171178f5d8b22d1a3396d9388adbb8ec1c0541@38.242.208.162:36656,ef8045e2922cf856b73f5fa5efdb79f925204ccf@65.109.117.159:15656,05b853c6022c51b2065665e66876e27aee9fed59@149.102.140.189:26656,94fdba93b79d27701896d65d8e60155e06326532@65.109.63.110:15656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.140:27126,6d59b44efa40c4a03a24bf598b6cd662e8003655@135.181.96.66:26656,00cedd85b1f6a2c859a8c6116b9578e1cc2623c6@51.222.44.116:30656,6aaf94803e3f387a3ee08b731890e6914e1e3419@65.108.233.102:30656,3b998a882d8d9bcb2869eef988af86254e0e9602@89.116.29.20:26656,b6dd58949a8b9c03349bdbec8aeeccd5e0d39283@31.220.74.50:26656,7ac17e470c16814be55aa02a1611b23a3fba3097@75.119.141.16:26656,1141119a7d248cc19b31b18d56162a365954deb9@45.132.106.149:26656,155b0aea2daadbb77e9eb1fbb235d2d81f7467c9@104.248.135.127:47656,9f7ecf77a52a56305c01fd072cdb79f0bc8b6660@194.163.169.45:26656,69e89a5169fef99ed1b72dadd4f5c7b801616c88@142.132.209.236:21256,0a9c34419331688b0b40d50fddbee286927602cb@5.78.79.97:26656,62f7aaafd73816bdaf685a6270541c1d1f8162ad@155.133.27.170:26656,c89e274523cec4a7445afaff1ab35029b090ff5b@65.109.116.204:20156,c4bb11ae43f4db7b8eef312a3c38861d236eb660@91.201.113.194:26656,e8f8c97c65b3e65797eca3489de7c1682e85d4df@78.25.143.46:47656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
