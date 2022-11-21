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

**live-peers** (25)
```
peers="7e0534cc92832ce8b499ffc662a9b73d2c0351a6@135.181.162.138:27001,e87b6771feff9f3c41e23a7c1e42b507345505fb@194.34.232.99:26656,3e5ba61e8481c6c71d3f2cc022dd6671ed7cacf8@65.21.170.3:41656,527c0753c83a5a89f5b51f50151b51a0d8638f7e@113.30.189.23:26656,c820e754c56b5455d64ab7685730c44a936d0833@154.38.165.129:26656,76895e84873db23aa366296acc6900e1dd980f43@195.201.237.185:22656,d159db085278927848c98b185b5871bf265669d9@185.250.36.169:41656,c312c6018fb7bb88bd73e03337e0bac4cfd7650b@82.208.20.196:26656,7d12df9de0cf5bff6148629897c3eb2d8589756b@65.109.84.215:60956,674a5a8d8f2a0815601bed562c46c060aa8ec075@65.109.70.4:60956,1989ced6b71ce676a5ab4d0586d85e38fd41fbd2@136.243.88.91:7070,a47375da7f790427c69103d363e4f8de4a6acfac@5.199.143.159:36656,ed9e3ea0d633fa27690f5d4db039403bbb1aeba8@165.22.214.209:26656,fe7af0c284fac131aa66448fafcc89e7f8298274@49.12.33.189:26656,a5369601c7a7e44a5fdc893540d706c87a48a58c@185.197.251.195:41656,bb6f0d3c55a6834037d545159869388bc498a5c7@144.76.90.130:27656,7a1c9ad925788a1811340b88068d6750c4511714@194.163.140.239:41656,61f824be9bdfe9a73b55ad162a9ed0bfe9121bbe@38.242.147.76:26656,cf31f6db36843f04675d694e6d79874d6acc3331@38.242.208.177:26656,481189b7e246f6c824a969482446c49abbfe76b8@161.97.172.147:26656,1d3bb209dfc7fe953fb8fa37774bab34016dd75c@185.245.183.85:26656,f6eeb6fa84ec13380f420af84fc293d00ad614ad@185.202.223.189:41656,5636d16da0732c451f4bb7fdc9be639b879c24d9@142.93.153.195:41656,5171aad5f862d474b36fc8049be3339068c96cc9@165.232.151.144:26656,7da6c90fe420bca73b5274884236134acf49d565@35.168.32.254:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.gitopia/config/config.toml
```
