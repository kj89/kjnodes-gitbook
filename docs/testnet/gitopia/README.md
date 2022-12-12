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

**live-peers** (35)
```
peers="6a7ba7eca935a76e02b5bbb9caf149a41da9af12@144.76.27.79:46656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:41656,c03e9f152bb1becc54d4424d02249135d39be09f@81.0.218.106:41656,980e2ec8f4ddba44e4a928452e49f3cae722fce3@65.21.182.244:27656,dea00215e54c4098a4f194a7ecd43e24ea99336f@88.99.95.81:26656,32254e5e11c49d8802f4c5bbd2c682eebd72ea33@80.241.220.28:60956,fccf79904b3c03488955d580509d0cc65bb3bb56@65.21.104.192:26656,c820e754c56b5455d64ab7685730c44a936d0833@154.38.165.129:26656,e79532749fb5dd95366f4568a7b2430d0e316fb5@84.46.255.163:26656,cf31f6db36843f04675d694e6d79874d6acc3331@38.242.208.177:26656,5ffdc1788f68df5e8163d9bd0d71a4c4d3dec2e9@81.0.220.21:26656,8f4c2887e46edc200a95afeaa87cb63bdddd26e2@185.239.208.131:656,730983044bcc3f8e688bc2436da8a171fd843922@154.12.243.189:656,023c6a86fbd8b8368503c92bd612a8c0379a26e5@194.146.13.251:656,6d36c85a0fc1d737906f47af2e090734e0f6d4a3@86.48.3.99:26656,075aa5cd1437de2a072878c347f9d4eb5849c842@86.48.5.165:26656,c84906b19dc7dc7bda94ab2167d4b0af64a28b49@45.151.122.191:656,f97115243c6291081b546e8d59f51e5ecede4168@149.102.155.225:26656,599bb15403aae7679ba59f878ee8b9c39264fc93@185.213.25.129:60956,1d3bb209dfc7fe953fb8fa37774bab34016dd75c@185.245.183.85:26656,d159db085278927848c98b185b5871bf265669d9@185.250.36.169:41656,4e0e57bcac8aa2bc3188d5b7845eeee61a61f3f0@194.163.170.165:26656,51c3b05112f73a6e60e8b2e96d5528a39a3f4e5e@38.242.246.96:26656,b44d4fd0799d2c06fbec0257b376c0520bdb226a@185.250.37.147:41656,5171aad5f862d474b36fc8049be3339068c96cc9@165.232.151.144:26656,91bf3eb973595dd4621ccf5853e5ac78c48058da@194.163.180.77:656,eb5fee5e8d7d5a300db7c89a4a24a205197f85c5@185.237.97.56:656,165c6969e40fa2ae2340d8e9fa79a14589a46406@185.193.66.202:26656,5c2c2b27e1824097d4f5dc7a581a8d615923e76f@185.252.235.110:41656,2f0484f05aa2d58d91aa21ea7cb9ce81c2e207ea@85.239.240.187:26656,965e495f4a69294bd85f3437fccdc9b210fd98b6@1.15.146.92:26656,0c37cd47e46901caadd8288a158edb81d37427a0@209.126.6.101:26656,2f58a44c9ce9dcdf81e2eaed7cd808ebefe222a7@38.242.243.111:26656,481189b7e246f6c824a969482446c49abbfe76b8@161.97.172.147:26656,8b0f39fa3739118578b49528321d4ea58399a755@144.217.201.174:41656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.gitopia/config/config.toml
```
