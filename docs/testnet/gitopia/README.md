# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/gitopia.png" width="150" alt=""><figcaption></figcaption></figure>

Gitopia is the next-generation Code Collaboration Platform fuelled by  a decentralized network and interactive token economy. It is designed  to optimize the open-source software development process through  collaboration, transparency, and incentivization.

**Chain ID**: gitopia-janus-testnet-2 | **Latest Version Tag**: v1.2.0 | **Wasm**: OFF

Website: [https://gitopia.com/](https://gitopia.com/)


## Public endpoints

* rpc: [https://gitopia-testnet.rpc.kjnodes.com](https://gitopia-testnet.rpc.kjnodes.com)
* api: [https://gitopia-testnet.api.kjnodes.com](https://gitopia-testnet.api.kjnodes.com)

## Peering

**state-sync**

```
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@gitopia-testnet.rpc.kjnodes.com:41656
```

**seed-node**

```
3f472746f46493309650e5a033076689996c8881@gitopia-testnet.rpc.kjnodes.com:41659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/gitopia-testnet/addrbook.json > $HOME/.gitopia/config/addrbook.json
```

**live-peers** (16)
```
peers="dbea2239b43c9e45913c22ad091abb8aaf7db469@75.119.159.159:33656,b7a2ef504e66b006ff29857fd85f1da4a40716d2@5.161.78.112:26656,2853f7582257f0a19854072906e21eb694aa05b4@80.79.6.253:26656,3a754aae8ee42a678b34a4393ff5bb658e43815e@137.184.165.200:41656,527c0753c83a5a89f5b51f50151b51a0d8638f7e@113.30.189.23:26656,9cd6d2477d278ef6ccffa5cc4e22fd0d9489cd23@85.10.199.157:34656,eec3daeed105dcd5647d1fc24ef8f1d0f404f2fe@167.235.21.149:29656,f1c042fca05e4bfb9a6da1cccaa5108a26ea1e0f@65.108.104.167:28656,ced37ae19b0cbb9b2bf6e18f6ac80957f630bc85@65.21.58.131:60956,0d1a964bbe844ab45a0ec93ffed81945e588f6b9@5.161.86.214:26656,d0d5136672e327c9f59402a08d24956d81ea66e0@188.166.87.208:26656,e87b6771feff9f3c41e23a7c1e42b507345505fb@194.34.232.99:26656,5171aad5f862d474b36fc8049be3339068c96cc9@165.232.151.144:26656,f786d8722a3f5b7dcc45714d0fc39ed088d6e2c5@94.250.203.3:6656,4fcd7fd0a9585f3ddc547ec7204b2bbafa35f2f2@185.92.148.124:36656,a5369601c7a7e44a5fdc893540d706c87a48a58c@185.197.251.195:41656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.gitopia/config/config.toml
```
