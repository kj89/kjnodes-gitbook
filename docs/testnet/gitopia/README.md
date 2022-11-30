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

**live-peers** (33)
```
peers="6d36c85a0fc1d737906f47af2e090734e0f6d4a3@86.48.3.99:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:41656,075aa5cd1437de2a072878c347f9d4eb5849c842@86.48.5.165:26656,1d3bb209dfc7fe953fb8fa37774bab34016dd75c@185.245.183.85:26656,f91f270980654a74c7619eff18bc068d2b86e6d8@54.90.149.14:41656,8a20f16d02806ba11bf9fab1fca91830578faa9e@161.97.151.46:46656,c630e7695e89074bf25a49afac7aca33feca9fd2@95.217.216.88:26656,2e714e8854361967515a8b859f8f4b0d9b8d11e8@194.163.190.86:26656,e9e671e22d794a4f80e32133905c83585b057a5d@86.48.3.0:26656,8710eb5025fd2cc370ec60fae079349aac2683c2@159.69.159.113:26656,63381c5528ed8ca93f9ba31008a9630d21b29a97@142.132.152.46:46656,4e0e57bcac8aa2bc3188d5b7845eeee61a61f3f0@194.163.170.165:26656,2f58a44c9ce9dcdf81e2eaed7cd808ebefe222a7@38.242.243.111:26656,27c172e3036cc778a592a418b818af271c2d3233@190.2.155.67:32656,fccf79904b3c03488955d580509d0cc65bb3bb56@65.21.104.192:26656,6a7ba7eca935a76e02b5bbb9caf149a41da9af12@144.76.27.79:46656,481189b7e246f6c824a969482446c49abbfe76b8@161.97.172.147:26656,a6f4fd8efe8a575a15e25652ecebce3fa1ed62a0@213.239.217.52:35656,bb6f0d3c55a6834037d545159869388bc498a5c7@144.76.90.130:27656,d159db085278927848c98b185b5871bf265669d9@185.250.36.169:41656,96fc6a8c3eb58d43c4ac41e9e642ba8485837ad3@109.123.255.116:26656,bbc6a1e115185d5bffcbbf5520dca1c3d626e599@109.123.255.50:26656,45de37d6340caef9bd84111ffb5163d0f3604e84@135.181.153.228:46656,73de34b1d08fdd58b5a5c0ec6d2560310c1ebe90@38.242.151.86:26656,c820e754c56b5455d64ab7685730c44a936d0833@154.38.165.129:26656,72678266f62ab7f0e79acfe9579701f12693dd7a@185.216.75.69:41656,98a1522fc5c2c200f8363ba5885771e7ec1ab5c7@95.217.211.32:26656,986afccee8c833afc2917075418474c1e9bf9fcb@65.109.82.75:26656,0d4c392f44c081347775643d99311bf2b36a7377@80.241.220.27:60956,54157f773b7135a134b1953d8c8a0ff128cad2f5@194.233.68.165:41656,1989ced6b71ce676a5ab4d0586d85e38fd41fbd2@136.243.88.91:7070,66f94651fb02f277c90c605a38df549d3c0a9269@75.119.151.217:26656,686e8d4b842a91cf63170de500d5351f49b440ce@206.189.0.110:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.gitopia/config/config.toml
```
