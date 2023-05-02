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
* grpc: andromeda-testnet.grpc.kjnodes.com:14790

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@andromeda-testnet.rpc.kjnodes.com:14756
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@andromeda-testnet.rpc.kjnodes.com:14759
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/andromeda-testnet/addrbook.json > $HOME/.andromedad/config/addrbook.json
```

**live-peers** (29)
```bash
peers="54188a9dea5ded1d891aa6c3c0e2a403322b1707@178.54.78.180:16656,c89e274523cec4a7445afaff1ab35029b090ff5b@65.109.116.204:20156,bd323d2c7ce260b831d20923d390e4a1623f32c4@213.239.215.195:20095,ef8045e2922cf856b73f5fa5efdb79f925204ccf@65.109.117.159:15656,443a51f595c9ca16273ca6146db1375e4223a91f@172.93.110.154:26656,05d3613dfb738ff22d0ea974bd0d1353ecdc6231@65.108.101.124:26656,1d94f397352dc20be4b56e4bfd9305649cbac778@65.108.232.150:20095,385bda41dc8ce86d0dd4c99d3cf371ca8fccfeb6@135.125.189.131:20095,e61f287d51edab6f6dbe00a8b804614443ee6f82@80.85.242.117:26656,36b5011de3c9bce6bbc7ff688525f432adff14ce@194.163.169.45:26656,00c49b6c8f0613bda77f27bf5072e4a000ace2b7@89.252.21.37:60556,8083dd301a7189284bf5b8d40c4cf239360d653a@5.9.122.49:26656,d30a56dd61de5b3e8d36bf40cb0a15add3915c91@195.3.223.33:37656,20373ec71cffdb678099ca411fb862537f264791@178.172.212.135:26656,9230896c5f22a363eed1c3bd3ed8068134b1dedd@115.87.238.93:26656,05b853c6022c51b2065665e66876e27aee9fed59@149.102.140.189:26656,27e4aeaf8ef79a25904cd1042cf25ac6a1a0e7e5@103.180.28.220:26656,717066f5726fb3cd7096f84911c7c8bfe5953e62@81.68.158.68:26656,7ba9cadf6197c30fa808d9315333054ef953be9c@144.76.164.139:15656,00171178f5d8b22d1a3396d9388adbb8ec1c0541@38.242.208.162:36656,1141119a7d248cc19b31b18d56162a365954deb9@45.132.106.149:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:47656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.140:27126,27752331150b966e3082e8dd8b364693379c1129@212.41.9.98:47656,28ce2dfb6c76e0baa660ec647bafe4a3b88cb3b0@94.131.118.190:26656,b6dd58949a8b9c03349bdbec8aeeccd5e0d39283@31.220.74.50:26656,7c9e768cdaa68d5c27b49797284acbd9d0dd9716@79.137.248.65:26656,3b998a882d8d9bcb2869eef988af86254e0e9602@89.116.29.20:26656,cdffce82a5f9f646f3e8e1cf66249b490303c431@47.5.80.5:26646"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
