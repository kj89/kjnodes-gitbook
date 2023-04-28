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

**live-peers** (27)
```bash
peers="3c5024a2213f8bae01e85f450e3d5eb11cf28768@95.217.188.65:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:47656,c89e274523cec4a7445afaff1ab35029b090ff5b@65.109.116.204:20156,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.140:27126,443a51f595c9ca16273ca6146db1375e4223a91f@172.93.110.154:26656,05d3613dfb738ff22d0ea974bd0d1353ecdc6231@65.108.101.124:26656,257491189415103312bcd203b1c6cd114d2cde9e@38.242.225.252:26656,00171178f5d8b22d1a3396d9388adbb8ec1c0541@38.242.208.162:36656,9230896c5f22a363eed1c3bd3ed8068134b1dedd@124.120.21.244:26656,ef8045e2922cf856b73f5fa5efdb79f925204ccf@65.109.117.159:15656,9e14886f7a34c73e65eafb209a9215e2848e9e76@65.108.41.172:29456,bd323d2c7ce260b831d20923d390e4a1623f32c4@213.239.215.195:20095,3b998a882d8d9bcb2869eef988af86254e0e9602@89.116.29.20:26656,cc1c2cd585792d81a041e9098e36814dc8d1e6ae@213.239.207.165:28756,1141119a7d248cc19b31b18d56162a365954deb9@45.132.106.149:26656,3d25f45062b5f3f49a87d38300ca0f657a9c853f@84.252.159.238:02656,fb7db0edee4ee43c2c65a81fd33e201c758d93df@137.184.176.247:47656,d3c2ce714e2c803d8686a0101711bf7164f844be@62.171.146.21:26656,b6dd58949a8b9c03349bdbec8aeeccd5e0d39283@31.220.74.50:26656,385bda41dc8ce86d0dd4c99d3cf371ca8fccfeb6@135.125.189.131:20095,828b8b74e88a974d16e2be8264f6537e87581aa3@5.189.168.185:26656,24971494b3a2045d26b111c85e1ea6baf15fece3@89.169.46.109:26656,69e89a5169fef99ed1b72dadd4f5c7b801616c88@142.132.209.236:21256,27e4aeaf8ef79a25904cd1042cf25ac6a1a0e7e5@103.180.28.220:26656,28ce2dfb6c76e0baa660ec647bafe4a3b88cb3b0@94.131.118.190:26656,139e89b8868aed5c5922a563ecd5002959af04ff@65.108.111.236:55716,7002fb6369cd13f8aa1520fd7a81e67a9adf2636@185.119.196.39:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
