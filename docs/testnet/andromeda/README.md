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
peers="0f966c78a7ac4722bd389f5c010efb8235ca8f73@65.108.227.112:14656,9230896c5f22a363eed1c3bd3ed8068134b1dedd@124.120.21.244:26656,c89e274523cec4a7445afaff1ab35029b090ff5b@65.109.116.204:20156,bd323d2c7ce260b831d20923d390e4a1623f32c4@213.239.215.195:20095,00171178f5d8b22d1a3396d9388adbb8ec1c0541@38.242.208.162:36656,385bda41dc8ce86d0dd4c99d3cf371ca8fccfeb6@135.125.189.131:20095,443a51f595c9ca16273ca6146db1375e4223a91f@172.93.110.154:26656,9e14886f7a34c73e65eafb209a9215e2848e9e76@65.108.41.172:29456,05d3613dfb738ff22d0ea974bd0d1353ecdc6231@65.108.101.124:26656,d0ef5f5583ff0343ea41962f68010bff54caafde@212.90.121.45:30656,54188a9dea5ded1d891aa6c3c0e2a403322b1707@178.54.78.180:16656,6d59b44efa40c4a03a24bf598b6cd662e8003655@135.181.96.66:26656,7002fb6369cd13f8aa1520fd7a81e67a9adf2636@185.119.196.39:26656,ef8045e2922cf856b73f5fa5efdb79f925204ccf@65.109.117.159:15656,32e94653d765d9a43eb9c7a97d752dd96b2a50d6@213.247.154.10:26656,0a9c34419331688b0b40d50fddbee286927602cb@5.78.79.97:26656,155b0aea2daadbb77e9eb1fbb235d2d81f7467c9@104.248.135.127:47656,05b853c6022c51b2065665e66876e27aee9fed59@149.102.140.189:26656,7ac17e470c16814be55aa02a1611b23a3fba3097@75.119.141.16:26656,28ce2dfb6c76e0baa660ec647bafe4a3b88cb3b0@94.131.118.190:26656,69e89a5169fef99ed1b72dadd4f5c7b801616c88@142.132.209.236:21256,1141119a7d248cc19b31b18d56162a365954deb9@45.132.106.149:26656,b6dd58949a8b9c03349bdbec8aeeccd5e0d39283@31.220.74.50:26656,c06d5254e4ecb69ccae41feff4d75de2dd92154d@149.102.138.176:26656,cfab4a4226372d11bf95b4aa1b1ece4e610a2185@5.75.162.210:26656,1d94f397352dc20be4b56e4bfd9305649cbac778@65.108.232.150:20095,27e4aeaf8ef79a25904cd1042cf25ac6a1a0e7e5@103.180.28.220:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:47656,e6707f1e650fab9cd82cc555224ee5ecfea7c9f5@89.58.16.33:47656,20248068f368f5d1eda74646d2bfd1fcdaffb3e1@89.58.59.75:60656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
