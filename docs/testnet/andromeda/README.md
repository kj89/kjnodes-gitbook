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

**live-peers** (30)
```bash
peers="8083dd301a7189284bf5b8d40c4cf239360d653a@5.9.122.49:26656,1d94f397352dc20be4b56e4bfd9305649cbac778@65.108.232.150:20095,13fddc7a47d1c4a381f5ffd6d9db3bda9eda154d@188.120.248.78:26656,c89e274523cec4a7445afaff1ab35029b090ff5b@65.109.116.204:20156,443a51f595c9ca16273ca6146db1375e4223a91f@172.93.110.154:26656,385bda41dc8ce86d0dd4c99d3cf371ca8fccfeb6@135.125.189.131:20095,00171178f5d8b22d1a3396d9388adbb8ec1c0541@38.242.208.162:36656,ef8045e2922cf856b73f5fa5efdb79f925204ccf@65.109.117.159:15656,05d3613dfb738ff22d0ea974bd0d1353ecdc6231@65.108.101.124:26656,bd323d2c7ce260b831d20923d390e4a1623f32c4@213.239.215.195:20095,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:47656,bc339c60d7a546ac42d9946b62b33588da99dda6@75.119.154.2:47656,1c101b595362f6a5856ef34f43545cf95eb34912@65.109.26.21:15656,9230896c5f22a363eed1c3bd3ed8068134b1dedd@115.87.238.93:26656,27e4aeaf8ef79a25904cd1042cf25ac6a1a0e7e5@103.180.28.220:26656,7649ae1ea0dd5f640ac7dd7632a0866cf65e3aa4@31.220.90.78:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.140:27126,05b853c6022c51b2065665e66876e27aee9fed59@149.102.140.189:26656,1141119a7d248cc19b31b18d56162a365954deb9@45.132.106.149:26656,fd48e41b990c9ba2cdd3e2f5adf20b8ab237b328@1.15.110.177:26656,27752331150b966e3082e8dd8b364693379c1129@212.41.9.98:47656,d3ac63ff921486f8aef1eba7870cae1d14c38633@1.15.146.92:26656,d30a56dd61de5b3e8d36bf40cb0a15add3915c91@195.3.223.33:37656,28ce2dfb6c76e0baa660ec647bafe4a3b88cb3b0@94.131.118.190:26656,e5a2bcbcea7d3b2ea7d7feb75da1c115125b665f@65.109.112.178:31656,36b5011de3c9bce6bbc7ff688525f432adff14ce@194.163.169.45:26656,ce3a765f7075f3f5aee80bca0c76ca7dbe235731@167.235.198.193:36656,704e605f9bd65912d8c65a58f955601c31188548@65.21.203.204:19656,03dc9e3ec16856653e0361f290a7580cf6b26a86@65.108.66.34:29556,9a40e9bb2f6d27ee36bb06908314c8052c923e94@80.76.43.138:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
