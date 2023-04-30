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

**live-peers** (30)
```bash
peers="91fde61878d704917f882694b271b67a38865ddc@149.102.142.94:26656,7c9e768cdaa68d5c27b49797284acbd9d0dd9716@79.137.248.65:26656,443a51f595c9ca16273ca6146db1375e4223a91f@172.93.110.154:26656,9230896c5f22a363eed1c3bd3ed8068134b1dedd@124.120.21.244:26656,cc1c2cd585792d81a041e9098e36814dc8d1e6ae@213.239.207.165:28756,c89e274523cec4a7445afaff1ab35029b090ff5b@65.109.116.204:20156,bd323d2c7ce260b831d20923d390e4a1623f32c4@213.239.215.195:20095,0a9c34419331688b0b40d50fddbee286927602cb@5.78.79.97:26656,05d3613dfb738ff22d0ea974bd0d1353ecdc6231@65.108.101.124:26656,1d94f397352dc20be4b56e4bfd9305649cbac778@65.108.232.150:20095,7ba9cadf6197c30fa808d9315333054ef953be9c@144.76.164.139:15656,ce3a765f7075f3f5aee80bca0c76ca7dbe235731@167.235.198.193:36656,c6c7256d80a5428aa1ab49a0417f9eb8422e8468@77.232.40.31:26656,1141119a7d248cc19b31b18d56162a365954deb9@45.132.106.149:26656,94fdba93b79d27701896d65d8e60155e06326532@65.109.63.110:15656,bc8a474a75951713263b2ed96105a70ad38804dc@1.15.131.138:26656,00171178f5d8b22d1a3396d9388adbb8ec1c0541@38.242.208.162:36656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.140:27126,ef8045e2922cf856b73f5fa5efdb79f925204ccf@65.109.117.159:15656,fb7db0edee4ee43c2c65a81fd33e201c758d93df@137.184.176.247:47656,385bda41dc8ce86d0dd4c99d3cf371ca8fccfeb6@135.125.189.131:20095,05b853c6022c51b2065665e66876e27aee9fed59@149.102.140.189:26656,d66cf29d246ed98290694418545914bb8c03c78b@65.108.215.65:26656,27e4aeaf8ef79a25904cd1042cf25ac6a1a0e7e5@103.180.28.220:26656,3b998a882d8d9bcb2869eef988af86254e0e9602@89.116.29.20:26656,25d712ffbb17e70a88d72b435f5d24729659ddc1@194.163.169.45:26656,327020664916aea0b66f3b1af348de030d53028f@194.34.232.99:26656,69e89a5169fef99ed1b72dadd4f5c7b801616c88@142.132.209.236:21256,811b1529b3ed9a4d5e704169ce95545f8b6c718c@82.208.23.192:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:47656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
